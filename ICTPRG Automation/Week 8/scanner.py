import socket

def is_valid_ip(ip):
    octets = ip.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        try:
            value = int(octet)
        except ValueError:
            return False
        if value < 0 or value > 255:
            return False
    return True

target = input("Enter an IP address: ")
if is_valid_ip(target):
    print("Valid IP address")
else:
    print("Invalid IP address")
    exit()

for port in range(1, 65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(3)
    result = s.connect_ex((target, port))
    if result == 0:
        print("Port {} is open".format(port))
    s.close()

