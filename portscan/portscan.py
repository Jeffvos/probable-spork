import ipaddress
import socket
from IPy import IP

def scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f'[+] Port {port} is open')
    except:
        print(f'[+] Failed port {port} closed')

if __name__ == "__main__":
    ipaddress = input('[+] Enter target ip ')
    port_start = int(input('[+] Start of the port range '))
    port_end = int(input('[+] End of the port range '))
    for port in range(port_start, port_end):
        scan(ipaddress=ipaddress, port=port)

