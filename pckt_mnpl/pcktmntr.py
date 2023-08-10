from scapy.all import *

def capture_packets(packet):
    if packet.haslayer(TCP):
        print("=" * 30)
        print("TCP Packet:")
        print("=" * 30)
        print(packet.show())

    if packet.haslayer(IP):
        print("=" * 30)
        print("IP Packet:")
        print("=" * 30)
        print(packet.show())

    if packet.haslayer(TCP) and packet.haslayer(Raw):
        payload = packet[Raw].load.decode("utf-8", errors="ignore")
        if "HTTP" in payload or "HTTPS" in payload:
            print("=" * 30)
            print("HTTP/HTTPS Packet:")
            print("=" * 30)
            print(payload)

def select_interface():
    print("Available network interfaces:")
    interfaces = get_windows_if_list() if os.name == "nt" else sorted(ifaces.data.keys())
    
    for i, iface in enumerate(interfaces, start=1):
        print(f"{i}. {iface}")

    choice = int(input("Select an interface by number: "))
    selected_interface = interfaces[choice - 1]
    return selected_interface

if __name__ == "__main__":
    iface = select_interface()
    print(f"Capturing packets on interface: {iface}")
    sniff(filter="ip or tcp", iface=iface, prn=capture_packets)
