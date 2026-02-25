from scapy.all import *
import gzip

def packet_callback(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        payload = packet[Raw].load
        try:
            decoded = payload.decode('utf-8')
            if 'GET' in decoded or 'POST' in decoded:
                print(f"[*] HTTP Packet: {decoded[:100]}...")
        except UnicodeDecodeError:
            pass

print("[*] Starting packet sniffing on port 80...")
packets = sniff(filter="tcp port 80", prn=packet_callback, store=1, timeout=300)
wrpcap("capture.pcap", packets)
print("[*] Sniffing completed. Packets saved to capture.pcap")
