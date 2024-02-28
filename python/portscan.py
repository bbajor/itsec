#!/bin/python3

from datetime import datetime
import socket
import sys

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Number of arguments not valid")
    print("Syntax: python3 portscan.py <ip-address>")


print("-" * 50)
print("Scanning target: " + target)
print("Scanning started at: " + str(datetime.now()))

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to server.")
    sys.exit()

finally:
    sys.exit()
