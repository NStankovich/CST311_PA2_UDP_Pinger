# Server.py
# We will need the following module to generate
# randomized lost packets
import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('127.0.0.1', 12000))
pingnum = 0
while True:
    # Count the pings received
    pingnum += 1
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the
    # address it is coming from
    message, address = serverSocket.recvfrom(1024)
    modifiedMessage = message.decode().upper()

    print(f"PING {pingnum} Recieved")
    print(f"Mesg rcvd: {message.decode()}")

    # If rand is less is than 4, and this not the
    # first "ping" of a group of 10, consider the
    # packet lost and do not respond

    if rand < 4 and pingnum % 10 != 1:
        print("Packet was lost.\n")
        continue

    # Otherwise, the server responds
    serverSocket.sendto(modifiedMessage.encode(), address)
    print(f"Mesg sent: {modifiedMessage}\n")
