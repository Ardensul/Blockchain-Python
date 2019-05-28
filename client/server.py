from socket import socket, gethostbyname, gethostname, AF_INET, SOCK_STREAM
from threading import Thread

clients = {}
addresses = {}

def accept_incoming_connections(socket):
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = socket.accept()
        print("Connection accepted from", client_address[0])
        addresses[client] = client_address
        Thread(target=handle_client, args=(client, client_address)).start()

def handle_client(client, client_address):
    """Handles a single client connection."""
    clients[client] = client_address
    while True:
        try:
            msg = client.recv(4096).decode()
            if not msg:
                client.close()
                print(clients[client][0], "has disconnected (Closed connection)")
                del clients[client]
                break
            else:
                print(client_address[0], ": ", msg, sep="")
        except ConnectionResetError:
            print(clients[client][0], "has disconnected (Connection reset by peer)")
            del clients[client]
            break
            

def run():
    host = gethostbyname(gethostname())
    port = input("Enter port: ")
    s = socket(AF_INET, SOCK_STREAM)
    s.bind( (( host, int(port) )) )
    
    s.listen(32)
    print("Server started on ", host, ":", port, sep="")
    conn = Thread(target=accept_incoming_connections, args=(s,))
    conn.start()
    conn.join()
    s.close()
