import socket
from sockets.router import route

def run_server():
    HOST = '127.0.0.1'
    PORT = 8080

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"Server ishlayapti: http://{HOST}:{PORT}")

    while True:
        client, addr = server.accept()

        request = client.recv(1024).decode()
        print(request)

        response = route(request)

        client.send(response.encode())
        client.close()