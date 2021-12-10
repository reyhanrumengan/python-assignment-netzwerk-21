import socket
import datetime
import time

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.settimeout(1) # wait for 1 second

address = ("127.0.0.1", 12000)
startTime = time.time()

for i in range(10):
    newTime = time.time()
    currentTime = datetime.datetime.fromtimestamp(newTime).strftime('%H:%M:%S')
    message = str.encode("ping " + currentTime)
    serverSocket.sendto(message, address)
    print(i+1, "Time: ", startTime)

    try:
        packet, server = serverSocket.recvfrom(1024)
        time_needed = newTime - startTime
        print(packet, time_needed)

    except socket.timeout:
        print('REQUEST END')










# from socket import *
# from time import time, ctime
# import sys
#
# # Inputs three arguments.
#
# if (len(sys.argv) != 3):
#     print(len(sys.argv))
#     print("Wrong number of arguments.")
#     print("Use: UDPPingClient.py <server_host> <server_port>")
#     sys.exit()
#
# # Preparing the socket
# serverHost, serverPort = sys.argv[1:]
# clientSocket = socket(AF_INET, SOCK_DGRAM)
# clientSocket.settimeout(1)
#
# # Send and receive 10 requests.
# for i in range(10):
#     startTime = time() # Retrieve the current time
#     message = "Ping " + str(i+1) + " " + ctime(startTime)[11:19]
#
#     try:
#
#         # Sending the message and waiting for the answer
#         clientSocket.sendto(message.encode(),(serverHost, int(serverPort)))
#         encodedModified, serverAddress = clientSocket.recvfrom(1024)
#
#         # Checking the current time and if the server answered
#         endTime = time()
#
#         # Modified message is  decoded.
#         modifiedMessage = encodedModified.decode()
#         print(modifiedMessage)
#
#         # Prints the RTT
#         print("Round Trip Time: %.3f ms\n" % ((endTime - startTime)*1000))
#     except:
#         print("PING %i Request timed out\n" % (i+1))
#
# clientSocket.close()


