import socket
 
TCP_IP = '0.0.0.0'
TCP_PORT = 1701

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
while True:
    data = conn.recv(31)
    print("received data:", data)
