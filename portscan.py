import ipaddress
import socket
from IPy import IP

ipaddress = input('[+] Enter the ip ')
port = int(input('[+] Port '))

try:
    sock = socket.socket()
    sock.connect((ipaddress, port))
    print(f'[+] Port {port} is open')
except:
    print(f'[+] Failed port {port} closed')