import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('localhost', 65400)
client_socket.connect(server_address)

try:
    while True:
        # Send data
        message = input("Enter message to send to server: ")
        client_socket.sendall(message.encode())

        # Receive response
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Server says: {data}")

except KeyboardInterrupt:
    print("\nConnection closed by client (Ctrl+C)")
finally:
    client_socket.close()
    print("Client shutdown.")
