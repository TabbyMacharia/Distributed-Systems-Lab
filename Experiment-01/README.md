# Experiment 1: Introduction to Distributed Systems

## Overview

This experiment introduces the fundamental concepts of **Distributed Systems** through the implementation of a simple client-server application using **Python sockets**.

The experiment demonstrates how independent components communicate over a network and explores several important concepts and challenges encountered in distributed systems, including:

* Client-server communication
* Socket-based communication
* Data transmission
* Request-response communication
* Multiple client connections
* Server unavailability and connection failure
* Communication delay and waiting time

The practical activities were implemented and tested using Python on a Windows environment.

---

## Learning Objectives

By completing this experiment, I aimed to:

1. Understand the basic concept of a distributed system.
2. Understand the roles of clients and servers.
3. Learn how sockets facilitate communication between distributed components.
4. Understand TCP-based client-server communication.
5. Implement one-way and two-way communication.
6. Observe how a server can accept multiple client connections.
7. Understand what happens when a server is unavailable.
8. Observe the effects of communication delays in a distributed application.

The experiment instructions specifically focus on understanding distributed systems, their characteristics, communication mechanisms, and challenges through a simple client-server application.

---

# Technologies Used

| Technology             | Purpose                                                             |
| ---------------------- | ------------------------------------------------------------------- |
| Python                 | Programming language used to implement the distributed applications |
| Python `socket` module | Network communication between client and server                     |
| TCP                    | Reliable connection-oriented communication protocol                 |
| PyCharm                | Development environment                                             |
| Windows PowerShell     | Running and testing the applications                                |
| Git & GitHub           | Version control and project documentation                           |

---

# Project Structure

The experiment was organized into separate folders for each activity so that the implementation and progression could be clearly tracked.

```text
Distributed-Systems-Lab/
│
├── Experiment-01/
│   │
│   ├── Activity-01/
│   │   ├── server.py
│   │   └── client.py
│   │
│   ├── Activity-02/
│   │   ├── server.py
│   │   └── client.py
│   │
│   ├── Activity-03/
│   │   ├── server.py
│   │   └── client.py
│   │
│   ├── Activity-04/
│   │   ├── server.py
│   │   └── client.py
│   │
│   ├── Activity-05/
│   │   ├── server.py
│   │   └── client.py
│   │
│   └── Activity-06/
│       ├── server.py
│       └── client.py
│
└── README.md
```

---

# Core Concepts

Before discussing each activity, it is important to understand the basic components used throughout the experiment.

## Client

The **client** is the component that initiates communication with the server.

In this experiment, the client:

1. Creates a socket.
2. Connects to the server.
3. Sends or receives data depending on the activity.
4. Closes the connection.

## Server

The **server** provides a service to the client.

In the experiments, the server:

1. Creates a socket.
2. Binds the socket to `localhost` and port `12345`.
3. Listens for incoming connections.
4. Accepts client connections.
5. Sends or receives data.
6. Closes the connection when communication is complete.

## Socket

A **socket** acts as an endpoint for communication between the client and server.

The applications used:

```python
socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
```

`AF_INET` specifies IPv4 addressing, while `SOCK_STREAM` specifies a TCP stream socket.

## Host and Port

The applications communicate using:

```text
localhost:12345
```

`localhost` refers to the local computer, while `12345` identifies the port on which the server listens for connections.

---

# Activity 1: Basic Client-Server Communication

## Objective

The first activity introduced basic communication between a client and a server using Python sockets.

The task required the server to send a message and the client to receive it.

## Communication Model

```text
Client                         Server
  |                              |
  |-------- connect() ---------->|
  |                              |
  |<------- "Hello from server" -|
  |                              |
  |-------- close() ------------>|
```

## Server Implementation

The server created a TCP socket, bound it to `localhost:12345`, listened for a connection, accepted the client, and sent a message.

```python
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

client_socket.send(b"Hello from server")

client_socket.close()
server_socket.close()
```

## Client Implementation

```python
import socket

client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client_socket.connect(("localhost", 12345))

data = client_socket.recv(1024)

print("Server says:", data.decode())

client_socket.close()
```

## Important Operations

### `bind()`

```python
server_socket.bind(("localhost", 12345))
```

Associates the server socket with the specified host and port.

### `listen()`

```python
server_socket.listen(1)
```

Places the server socket into a listening state so that it can accept incoming connections.

### `accept()`

```python
client_socket, address = server_socket.accept()
```

Waits for a client to connect.

### `connect()`

```python
client_socket.connect(("localhost", 12345))
```

Allows the client to initiate a connection to the server.

### `send()`

```python
client_socket.send(b"Hello from server")
```

Sends data through the established socket connection.

### `recv()`

```python
data = client_socket.recv(1024)
```

Receives data from the socket.

### `encode()` and `decode()`

Sockets transmit data as bytes.

The server therefore sends:

```python
b"Hello from server"
```

The client converts the received bytes into a string using:

```python
data.decode()
```

## Result

The server successfully accepted the client connection and sent a message. The client successfully received and displayed the message.

### Observation

| Experiment          | Observation                                                                        | Result     |
| ------------------- | ---------------------------------------------------------------------------------- | ---------- |
| Basic Communication | The client connected to the server and successfully received the server's message. | Successful |

---

# Activity 2: Modify the Message

## Objective

The second activity demonstrated how data transmitted between distributed components can be modified while maintaining the same communication mechanism.

The message sent by the server was changed from the original message to:

```text
Welcome to Distributed Systems Laboratory
```

The client code did not need to be changed.

## Why the Client Did Not Need Modification

The client was already configured to:

1. Connect to `localhost`.
2. Use port `12345`.
3. Receive data from the server.
4. Decode the received bytes.

It did not need to know the exact contents of the message beforehand.

The server could therefore change:

```python
client_socket.send(b"Hello from server")
```

to:

```python
client_socket.send(
    b"Welcome to Distributed Systems Laboratory"
)
```

and the same client could receive the new message.

## Key Concept

This activity demonstrated that the socket provides the **communication channel**, while the actual message is application data transmitted through that channel.

The socket transmits bytes, which are then decoded by the receiving application.

## Result

The modified message was successfully transmitted from the server and displayed by the client.

### Observation

| Experiment           | Observation                                                                                                                                           | Result     |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| Message Modification | The server message was changed while the client continued using the same connection configuration. The client successfully displayed the new message. | Successful |

---

# Activity 3: Two-Way Communication

## Objective

The third activity introduced **request-response communication**.

The client was modified to send a message to the server. The server received and displayed the message and then sent a response back to the client.

## Communication Model

Unlike Activity 1, which mainly demonstrated:

```text
Server ─────────► Client
```

Activity 3 demonstrated:

```text
Client ─────────► Server
       Request

Client ◄───────── Server
       Response
```

## Server Communication Sequence

The server:

1. Accepted the client connection.
2. Received the client's message.
3. Decoded and displayed the message.
4. Sent a response.
5. Closed the connection.

The important sequence was:

```python
data = client_socket.recv(1024)

print("Client says:", data.decode())

client_socket.send(
    b"Hello Client, message received!"
)
```

## Client Communication Sequence

The client:

1. Connected to the server.
2. Sent a message.
3. Waited for the server's response.
4. Displayed the response.

```python
client_socket.send(b"Hello Server!")

data = client_socket.recv(1024)

print("Server says:", data.decode())
```

## Important Lesson: Communication Order

The order of communication is important.

The client sends first:

```text
Client                         Server
  |                              |
  |-------- message ------------>|
  |                              |
  |<-------- response -----------|
```

If both sides wait at `recv()` before either side sends, both programs can remain blocked waiting for data from the other side.

This demonstrated that distributed components must follow an agreed **communication protocol or sequence**.

## Result

The client successfully sent a message to the server, and the server responded to the client.

### Observation

| Experiment            | Observation                                                                                            | Result     |
| --------------------- | ------------------------------------------------------------------------------------------------------ | ---------- |
| Two-Way Communication | The client sent a message, the server received it and returned a response, which the client displayed. | Successful |

---

# Activity 4: Multiple Client Connections

## Objective

The fourth activity demonstrated how a server can handle multiple users by accepting multiple client connections. The instructions required the server to be modified and several client terminals to be used.

## Server Modification

The server was changed to continuously accept clients using:

```python
while True:
    client_socket, address = server_socket.accept()

    print("Client connected:", address)

    client_socket.send(b"Hello from server!")

    client_socket.close()
```

The server also increased its listening backlog:

```python
server_socket.listen(5)
```

## Why `while True` Was Used

Without the loop, the server would accept one client and then terminate.

With:

```python
while True:
```

the server continues running and can accept additional connections.

## Testing

Three clients were connected to the server.

The server produced:

```text
Server is waiting for clients...
Client connected: ('127.0.0.1', 62441)
Client connected: ('127.0.0.1', 62442)
Client connected: ('127.0.0.1', 62443)
```

Each client successfully received the server's message.

## Understanding the Addresses

The server displayed addresses such as:

```text
('127.0.0.1', 62441)
```

Here:

* `127.0.0.1` represents `localhost`.
* `62441` is a temporary client-side port.
* Each client connection received a different temporary port.

The server itself continued listening on:

```text
localhost:12345
```

## Important Limitation

Although this activity successfully demonstrated **multiple client connections**, the implementation handled them **sequentially**.

The server accepts a client, sends the message, closes the connection, and then accepts the next client.

True simultaneous/concurrent handling would require mechanisms such as threads or processes. This becomes relevant in later distributed-systems experiments.

## Result

Three clients successfully connected to the server and each received the server's message.

### Observation

| Experiment       | Observation                                                                                                                                | Result     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| Multiple Clients | Three clients connected successfully. Each connection had a different temporary client port and each client received the server's message. | Successful |

---

# Activity 5: Network Failure Simulation

## Objective

The fifth activity introduced a failure scenario by running the client **without starting the server**. The purpose was to understand fault-tolerance challenges in distributed systems.

## Experiment Setup

The client attempted to connect to:

```text
localhost:12345
```

However, the server was not running.

Therefore, there was no application listening on port `12345`.

## Observed Error

The client generated:

```text
Traceback (most recent call last):
  File "C:\Users\ADMIN\PycharmProjects\Distributed-Systems-Lab\Experiment-01\Activity-05\client.py", line 8, in <module>
    client_socket.connect(("localhost", 12345))
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it
```

## Explanation

The failure occurred at:

```python
client_socket.connect(("localhost", 12345))
```

The client could not establish the TCP connection because no server process was listening on port `12345`.

The `recv()` operation was therefore never reached.

## Communication Model

```text
Client
   |
   | connect(localhost:12345)
   |
   X
Server unavailable
   |
Connection refused
```

## Distributed Systems Concept

This activity demonstrated **failure and availability**.

A distributed system cannot assume that all components will always be available. A server may be stopped, unavailable, unreachable, or unable to accept a connection.

Real distributed systems therefore need mechanisms for handling failures, such as error handling, timeouts, retries, or alternative services.

## Result

The expected connection failure occurred and the `ConnectionRefusedError` was successfully observed and documented.

### Observation

| Experiment         | Observation                                                                                                               | Result                        |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| Server Unavailable | The client attempted to connect while the server was not running and received `ConnectionRefusedError: [WinError 10061]`. | Connection failed as expected |

---

# Activity 6: Communication Delay Experiment

## Objective

The sixth activity demonstrated **network latency and waiting time** in distributed systems by introducing a deliberate delay before the server sent its message. The experiment instructions specified adding `time.sleep(5)` before the server's send operation.

## Implementation

The following modules and statement were added:

```python
import time
```

and:

```python
time.sleep(5)
```

The delay was placed immediately before sending the response:

```python
time.sleep(5)

client_socket.send(
    b"Hello from server after 5 seconds!"
)
```

## Why the Delay Was Placed Before `send()`

The purpose was to simulate a situation where the server takes time before producing a response.

The sequence became:

```text
accept()
   ↓
Client connected
   ↓
sleep(5)
   ↓
send()
   ↓
Client receives message
```

## Client Behavior

The client successfully connected to the server and then reached:

```python
data = client_socket.recv(1024)
```

Since the server had not yet sent the message, the client waited.

After approximately five seconds, the server sent the message and the client displayed:

```text
Server says: Hello from server after 5 seconds!
```

## Observed Server Output

```text
Server is waiting for a connection...
Client connected: ('127.0.0.1', 51883)
Waiting for 5 seconds before sending...
```

## Observed Client Output

```text
Connected to server. Waiting for message...
Server says: Hello from server after 5 seconds!
```

## Distributed Systems Concept

This activity demonstrated the difference between:

**Connection failure**

and

**Communication delay**

In Activity 5, the connection itself failed because the server was unavailable.

In Activity 6, the connection was successfully established, but the response was delayed.

```text
Activity 5

Server unavailable
       ↓
Connection fails
       ↓
ConnectionRefusedError


Activity 6

Server available
       ↓
Connection succeeds
       ↓
Server delays response
       ↓
Client waits
       ↓
Message received
```

## Result

The five-second delay was successfully introduced. The client remained connected and waited for the server's response before displaying the message.

### Observation

| Experiment          | Observation                                                                                                            | Result                          |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| Communication Delay | The server delayed its response by approximately five seconds. The client remained waiting until the message was sent. | Delay successfully demonstrated |

---

# Overall Observation Table

| Activity   | Main Concept                      | Observation                                                              | Result                       |
| ---------- | --------------------------------- | ------------------------------------------------------------------------ | ---------------------------- |
| Activity 1 | Basic Client-Server Communication | Client successfully connected to server and received a message.          | Successful                   |
| Activity 2 | Message Modification              | Server message was modified and the client received the updated message. | Successful                   |
| Activity 3 | Two-Way Communication             | Client sent a message and received a response from the server.           | Successful                   |
| Activity 4 | Multiple Clients                  | Three clients successfully connected to the server.                      | Successful                   |
| Activity 5 | Network Failure                   | Client generated `ConnectionRefusedError` when server was unavailable.   | Failure observed as expected |
| Activity 6 | Communication Delay               | Client waited while the server delayed its response by five seconds.     | Delay observed successfully  |

---

# Key Lessons Learned

## 1. Distributed components communicate through defined interfaces

The client and server are separate components that communicate through a socket connection.

## 2. TCP provides connection-oriented communication

The applications used:

```python
socket.AF_INET
socket.SOCK_STREAM
```

to create an IPv4 TCP socket.

## 3. Communication requires coordination

In two-way communication, both sides must follow an agreed sequence of sending and receiving messages.

## 4. Multiple users introduce additional challenges

A server that accepts multiple clients must be designed to manage those connections appropriately. The Activity 4 implementation demonstrated repeated connections, while true concurrent processing requires additional mechanisms.

## 5. Distributed systems must account for failure

Activity 5 demonstrated that a client cannot establish communication when the server is unavailable.

## 6. Delay affects distributed communication

Activity 6 demonstrated that even when a connection is successful, a delay in receiving a response can cause a client to wait.

---

# Challenges Encountered and Resolved

### 1. Understanding `send()` and `recv()`

Initially, it was necessary to understand that socket communication involves sending and receiving bytes rather than directly transmitting Python strings.

This was resolved by using:

```python
send()
```

for transmission and:

```python
decode()
```

after receiving data.

### 2. Understanding communication order

During two-way communication, reversing the expected send/receive sequence caused both sides to wait for data.

This demonstrated why distributed applications need a clearly defined communication sequence.

### 3. Understanding multiple client ports

When several clients connected, each connection showed a different temporary client port even though the server continued listening on port `12345`.

This helped distinguish the **server's listening port** from the **client's temporary port**.

### 4. Understanding connection failure

Activity 5 produced:

```text
ConnectionRefusedError: [WinError 10061]
```

This demonstrated that the absence of a listening server prevents the TCP connection from being established.

### 5. Understanding communication delay

Activity 6 demonstrated that a successful connection does not necessarily mean an immediate response. The client may remain blocked at `recv()` while waiting for data.

---

# Conclusion

Experiment 1 provided a practical introduction to distributed systems by implementing client-server communication using Python sockets.

Starting with basic one-way communication, the experiment progressively introduced message modification, two-way request-response communication, multiple client connections, server failure, and communication delay.

The most important lesson from the experiment was that distributed systems involve more than simply connecting computers. Components must communicate using defined protocols, coordinate their interactions, handle multiple users, tolerate failures, and account for delays in communication.

Through the six activities, I gained practical experience with Python socket programming and developed a better understanding of how communication, failure, and delay affect distributed applications.
