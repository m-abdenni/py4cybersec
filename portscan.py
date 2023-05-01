import sys
import socket
import pyfiglet
import threading

banner = pyfiglet.figlet_format("Python Port Scanner")
print(banner)

if len(sys.argv) < 2:
    exit()

ip = sys.argv[1]
ports = range(1, 65535)
open_ports = []

def port_scan(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            print(f'[+] Open {port}')
            open_ports.append(port)
    except Exception as e:
        pass

threads = []

for port in ports:
    t = threading.Thread(target=port_scan, args=(ip, port))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"Scanning completed. Open ports: {open_ports}")
