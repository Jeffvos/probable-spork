import ipaddress
import socket
from IPy import IP

def target_scan(target):
    conv_ip = validate_ip(target)

def scan(ipaddress, port):
    try:
        validated_ip = validate_ip(ipaddress)
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((validated_ip, port))
        print(f'[+] Port {port} is open - {ipaddress}')
    except:
        print(f'[-] Failed port {port} closed - {ipaddress}')

def validate_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


if __name__ == "__main__":
    target = input('[+] Enter target(s) ip, (use , to specify multiple targets): ')
    port_start = int(input('[+] Start of the port range: '))
    port_end = int(input('[+] End of the port range: ')) + 1
    if ',' in target:
        for ipadd in target.split(','):
            for port in range(port_start, port_end):
                scan(ipaddress=ipadd.strip(' '), port=port)
    else:
        for port in range(port_start, port_end):
            scan(ipaddress=target, port=port)

    

