import ipaddress
import socket
from IPy import IP


class PortScan:
    def __init__(self, target, port):
        self.target = target
        self.port = port


    def target_scan(self):
        conv_ip = validate_ip(self.target)

    def scan(self):
        try:
            validated_ip = validate_ip(self.target)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            sock.connect((validated_ip, self.port))
            try:
                banner = get_banner(sock)
                print(f'[+] Port {self.port} is open - {self.target} - {banner}')
            except:
                print(f'[+] Port {self.port} is open - {self.target}')
        except:
            print(f'[-] Failed port {self.port} closed - {self.target}')

    def get_banner(self, so):
        print(f'so {so.recv(1024).decode()}')
        return so.recv(1024).decode()

    def validate_ip(self, ip):
        try:
            IP(ip)
            return ip
        except ValueError:
            return socket.gethostbyname(ip)