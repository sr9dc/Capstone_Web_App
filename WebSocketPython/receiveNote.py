# Implemented by Server, will be running on MSP 430 Booster Pack
import socket

# Input the Server and Port of the MSP
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# Set up Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    # Receive Data Message from Client
    data, addr = sock.recvfrom(1024)
    x = data 
    print("received message: %s" % x)

    print("length of msg: ", len(x))