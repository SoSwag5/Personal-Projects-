import socket
from datetime import datetime

def port_scanner(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Set a timeout for the connection attempt / To make the connection faster
        if s.connect_ex((host, port)):
            print(f"Port {port} is open on {host}.")
        else:
            print(f"Port {port} is closed on {host}.")
    finally:
        s.close()

host = input("Please enter the Ip you want to scan: ")
ports = [80, 20, 40]

for port in ports:
    port_scanner(host, port)
