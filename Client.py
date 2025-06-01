import socket
import sys

if len(sys.argv) != 4:
    print("Usage: python Client.py <server_host> <server_port> <filename>")
    sys.exit()

host = sys.argv[1]
port = int(sys.argv[2])
filename = sys.argv[3]

try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((host, port))

    # This line simulates a basic TCP request (not real HTTP)
    clientSocket.send(filename.encode())

    print(f"[CLIENT] Go to -> http://{host}:{port}/{filename}")

    response = b""
    while True:
        chunk = clientSocket.recv(1024)
        if not chunk:
            break
        response += chunk

    print("[SERVER RESPONSE]")
    print(response.decode(errors='ignore'))

    clientSocket.close()

except Exception as e:
    print(f"Error connecting to {host}:{port}\n{e}")
