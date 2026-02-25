from scapy.all import *
import re

def analyze_pcap(pcap_file):
    packets = rdpcap(pcap_file)
    xss_found = False
    for packet in packets:
        if packet.haslayer(TCP) and packet.haslayer(Raw):
            payload = packet[Raw].load.decode('utf-8', errors='ignore')
            if 'GET' in payload or 'POST' in payload:
                print(f"HTTP Request:\n{payload[:500]}...\n")
            if re.search(r'<script.*?>.*?</script>', payload, re.IGNORECASE) or \
               re.search(r'onerror=".*?"', payload, re.IGNORECASE):
                print("[!] XSS payload detected in packet!")
                xss_found = True
    if not xss_found:
        print("[*] No XSS payloads detected in the captured traffic.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python analyze_pcap.py <pcap_file>")
        sys.