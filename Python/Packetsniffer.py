from scapy.all import sniff, conf
from scapy.layers.l2 import Ether

def process_packet(packet):
    if Ether in packet:
        print(packet.summary())

# Print available interfaces with details
print("Available interfaces with details:")
interfaces = conf.ifaces
for iface in interfaces.values():
    print(f"Index: {iface.index}, Name: {iface.name}, Description: {iface.description}")
USER = input("What interface do you want to sniff *wink* *wink*: ")
# Define the network interface you want to sniff on
# Replace 'YOUR_INTERFACE_NAME' with the name of the interface you want to use
interface = USER

try:
    # Start sniffing using scapy's sniff function with the correct interface name
    sniff(iface=interface, filter="ip", prn=process_packet, store=0)
except KeyboardInterrupt:
    print("Sniffing has ended")
except OSError as e:
    print(f"An error occurred: {e}")
