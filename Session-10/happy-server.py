import socket

PORT = 8080  # Configure the Server's IP and PORT
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Step 1: create the socket
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # For avoiding the problem of Port
ls.bind((IP, PORT))  # Step 2: Bind the socket to server's IP and PORT
ls.listen()  # Step 3: Configure the socket for listening
print("The server is configured!")

while True:
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)  # Read the message from the client in raw bytes
        msg = msg_raw.decode()  # Decode it for converting it into a human-redeable string
        print(f"Message received: {msg}")
        response = "HELLO. I am the Happy Server :-)\n"   # Response message to the client
        cs.send(response.encode())  # -- The message has to be encoded into bytes
        cs.close()