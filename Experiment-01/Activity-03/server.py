import socket

server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server_socket.bind(("localhost", 12345))

server_socket.listen(1)

print("Server is waiting for a connection...")

client_socket, address = server_socket.accept()

print("Client connected:", address)

data = client_socket.recv(1024)

print("Client says:", data.decode())

client_socket.send(b"Hello Client, message received!")

client_socket.close()
server_socket.close()