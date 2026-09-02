import socket
import time

server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server_socket.bind(("localhost", 12345))

server_socket.listen(1)

print("Server is waiting for a connection...")

client_socket, address = server_socket.accept()

print("Client connected:", address)

print("Waiting for 5 seconds before sending...")

time.sleep(5)

client_socket.send(b"Hello from server after 5 seconds!")

client_socket.close()
server_socket.close()