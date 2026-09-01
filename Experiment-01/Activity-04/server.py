import socket

server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server_socket.bind(("localhost", 12345))

server_socket.listen(5)

print("Server is waiting for clients...")

while True:
    client_socket, address = server_socket.accept()

    print("Client connected:", address)

    client_socket.send(b"Hello from server!")

    client_socket.close()