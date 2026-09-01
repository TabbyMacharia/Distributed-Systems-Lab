import socket

client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client_socket.connect(("localhost", 12345))

data = client_socket.recv(1024)

print("Received Message:", data.decode())

client_socket.close()