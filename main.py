import socket
import threading
from datetime import datetime
import subprocess


print("-" * 70)



print("-" * 70)
print("-" * 70)

host = socket.gethostbyname(input("[+] Enter target domain: ", ))
start_port = int(input("[+] Enter start port: "))
end_port = int(input("[+] Enter end port: "))

print("-" * 50)
print("Scanning Target: " + host)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)


def scan(port):
    s = socket.socket()
    s.settimeout(3)
    result = s.connect_ex((host, port,))
    if result == 0:
        print("Port {} is open".format(port, ))
    s.close()


for i in range(start_port, end_port + 1):
    t = threading.Thread(target=scan, args=(i,))
    t.start()