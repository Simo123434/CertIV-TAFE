import socket
import threading

def scan_port(ip, port, open_ports):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
            open_ports.append(port)
        sock.close()
    except Exception as e:
        pass

ip = input("Enter an IP address: ")
open_ports = []

for port in range(1, 65535):
    thread = threading.Thread(target=scan_port, args=(ip, port, open_ports))
    thread.start()

for thread in threading.enumerate():
    if thread != threading.current_thread():
        thread.join()

if len(open_ports) > 0:
    print(f"\nOpen ports: {open_ports}")
else:
    print("No open ports found")
