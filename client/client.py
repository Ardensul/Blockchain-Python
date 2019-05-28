from socket import socket, AF_INET, SOCK_STREAM, SHUT_WR
from threading import Thread

class Tx():
    """Client side of the peer"""
    def __init__(self, remote, rport=7777):
        self.remote = remote
        self.rport = rport
        self.sock = socket(AF_INET, SOCK_STREAM)
        try:
            self.sock.connect((self.remote, self.rport))
            print("Connected to", self.remote)
        except ConnectionRefusedError:
            print("Unable to connect to", self.remote)

    def send(self, msg):
        self.sock.send( msg.encode() )

    def close(self):
        self.sock.shutdown(SHUT_WR)
        self.sock.close()

    def status(self):
        print("Tx to", self.remote, "on port", self.rport)
        try:
            self.send("ping")
            print("Status: alive")
        except:
            print("Status: dead")

def run():
    isConnected = False
    x = 0

    while not isConnected:
        ip = input("Enter IP: ")
        port = input("Enter port: ")

        try:
            tx = Tx(ip, (int)(port))
            x = 1
        except TimeoutError:
            print("Connection timed out")
        except ConnectionRefusedError:
            print("Connection refused")

        if x == 1:
            isConnected = True

    while True:
        msg = input("Enter msg: ")
        if len(msg) == 0:
            tx.close()
            break
        else:
            tx.send(msg)
