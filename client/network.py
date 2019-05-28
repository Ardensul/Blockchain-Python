import socket, threading

def checkIfMinerRunning():
    """Kind of an obviously named function, innit ?"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect(("127.0.0.1", 7777))
    sock.close()

    if result == 0:
        return True
    else:
        return False

class Rx(threading.Thread):
    """Server side of the peer"""
    def __init__(self, port=7777, bufsize=4096):
        threading.Thread.__init__(self, name="rx")
        self.host = "127.0.0.1"
        self.port = port
        self.bufsize = bufsize
        # Build socket during init
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen()
        print("Server started on port", self.port)
        while True:
            conn, client_addr = self.sock.accept()
            print("Connection accepted from", client_addr[0])
            try:
                while True:
                    data = conn.recv(self.bufsize)

                    if not data:
                        break
                    print(client_addr[0], ":", data.decode())
            except:
                continue
            finally:
                conn.shutdown(socket.SHUT_RD)
                conn.close()

    def run(self):
        # Needs to be run asynchronously
        self.listen()

class Tx(threading.Thread):
    """Client side of the peer"""
    def __init__(self, remote, rport=7777):
        threading.Thread.__init__(self, name="tx")
        self.remote = remote
        self.rport = rport
        # Same as Rx but with exception catching this time
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((self.remote, self.rport))
            print("Connected to", self.remote)
        except ConnectionRefusedError:
            print("Unable to connect to", self.remote)

    def send(self, msg):
        self.sock.send( msg.encode() )

    def close(self):
        self.sock.shutdown(socket.SHUT_WR)
        self.sock.close()

    def status(self):
        print("Tx to", self.remote, "on port", self.rport)
        try:
            self.send("ping")
            print("Status: alive")
        except:
            print("Status: dead")

class Endpoint:
    """The peer itself, in all its glory of a few hundred bytes"""
    def __init__(self):
        self.rx = Rx()
        self.peers = []

    def addPeer(self, ip):
        self.peers.append( Tx(ip) )

    def removePeer(self, ip):
        for peer in range(len(self.peers)):
            if ip == peer.ip:
                self.peers.pop(peer)
