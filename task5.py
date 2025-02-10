from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime
import argparse
import sys

class PacketSniffer:
    def __init__(self, interface=None, pcap_file=None):
        self.interface = interface
        self.pcap_file = pcap_file
        self.packet_count = 0
        self.protocols = {
            'TCP': 0,
            'UDP': 0,
            'Other': 0
        }

    def packet_callback(self, packet):
        self.packet_count += 1
        print(f"\n{'='*60}")
        print(f"Packet #{self.packet_count} captured at {datetime.now()}")
        
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            protocol = packet[IP].proto
            
            print(f"\nIP Header:")
            print(f"Source IP: {src_ip}")
            print(f"Destination IP: {dst_ip}")
            
            if TCP in packet:
                self.protocols['TCP'] += 1
                print("\nTCP Header:")
                print(f"Source Port: {packet[TCP].sport}")
                print(f"Destination Port: {packet[TCP].dport}")
                print(f"Flags: {packet[TCP].flags}")
                
            elif UDP in packet:
                self.protocols['UDP'] += 1
                print("\nUDP Header:")
                print(f"Source Port: {packet[UDP].sport}")
                print(f"Destination Port: {packet[UDP].dport}")
            
            else:
                self.protocols['Other'] += 1
                print(f"\nProtocol: {protocol}")
            
            if packet.haslayer('Raw'):
                payload = packet['Raw'].load
                print("\nPayload Preview (first 100 bytes, hex):")
                print(payload[:100].hex())
        
        print(f"\nRunning Statistics:")
        print(f"Total Packets: {self.packet_count}")
        for proto, count in self.protocols.items():
            print(f"{proto} Packets: {count}")

    def start_sniffing(self, packet_count=None):
        try:
            print(f"Starting packet capture...")
            print(f"Interface: {self.interface or 'default'}")
            print(f"Press Ctrl+C to stop capturing\n")
            
            sniff(
                iface=self.interface,
                prn=self.packet_callback,
                count=packet_count,
                store=0
            )
            
        except KeyboardInterrupt:
            print("\nPacket capture stopped by user")
        except Exception as e:
            print(f"\nError: {e}")
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Network Packet Sniffer for Educational Purposes')
    parser.add_argument('-i', '--interface', help='Network interface to capture packets')
    parser.add_argument('-c', '--count', type=int, help='Number of packets to capture')
    args = parser.parse_args()

    sniffer = PacketSniffer(interface=args.interface)
    sniffer.start_sniffing(packet_count=args.count)

if __name__ == "__main__":
    main()
