import socket

UDP_IP = "0.0.0.0"

ipsec_ike = socket.socket(socket.AF_INET, # Internet
                          socket.SOCK_DGRAM) # UDP
ipsec_ike.bind((UDP_IP, 500))
ipsec_nat = socket.socket(socket.AF_INET, # Internet
                          socket.SOCK_DGRAM) # UDP
ipsec_nat.bind((UDP_IP, 5500))

while True:
    print("received message nat:", ipsec_nat.recvfrom(2))
    print("received message ike:", ipsec_ike.recvfrom(2))