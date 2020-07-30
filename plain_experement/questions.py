import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s.bind(('127.0.0.1', 1701))  # L2TP
except:
    s.close()
    sys.exit(1)

print('Server is up and listening at', s.getsockname())

while True:
    data, address = s.recvfrom(MAX)
    s.sendto(str(i), address)
    data, address = s.recvfrom(MAX)
