import nmap




scanner = nmap.PortScanner()
print("Welcome, this is a simple Nmap automation tool")
print("<-------------------------------------------------->")
ipaddr = input("Please enter an ipaddress you want to scan: ")
print(f"The Ip entered is {ipaddr}")
type(ipaddr)

resp = input("""Please enter the type of scan you want to run
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan
                ------> """)

print(f"The selected option is {resp}")

if resp == '1':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ipaddr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    #Then we display if the ip is reachable or not reachable using the state
    print("Ip Status: ", scanner[ipaddr].state())
    #we are displaying what protocols we are scanning for
    print(scanner[ipaddr].all_protocols())
    #return all the active port or all the port that are reachable within a specificed range
    print("Open ports :", scanner[ipaddr]['tcp'].keys())
elif resp == '2':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ipaddr, '1-1024', '-v -sU') #Change to sU to scan for udp ports
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ipaddr].state())
    print(scanner[ipaddr].all_protocols())
    print("Open ports :", scanner[ipaddr]['udp'].keys()) #change the tcp to udp
elif resp == '3': #comprehensive scan == Full scan
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ipaddr, '1-5000', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ipaddr].state())
    print(scanner[ipaddr].all_protocols())
    print("Open ports :", scanner[ipaddr]['tcp'].keys())
else:
    print("Enter a valid option! ")
    