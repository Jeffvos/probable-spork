import ipaddress
import socket
from IPy import IP

def scan(ipaddress, port):
    try:
        validated_ip = validate_ip(ipaddress)
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((validated_ip, port))
        print(f'[+] Port {port} is open')
    except:
        print(f'[-] Failed port {port} closed')

def validate_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


if __name__ == "__main__":
    ipaddress = input('[+] Enter target ip ')
    port_start = int(input('[+] Start of the port range '))
    port_end = int(input('[+] End of the port range ')) + 1
    for port in range(port_start, port_end):
        scan(ipaddress=ipaddress, port=port)

