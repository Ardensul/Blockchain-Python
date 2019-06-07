import json
import socket
from threading import Thread

from requests import get

from blochain.Chain import Chain
from blochain.Transcation import Transaction

ip = get('https://api.ipify.org').text
chain = Chain()
transaction = Transaction()


class ListenChain(Thread):

    def __init__(self, port, ip, chain, transaction):
        Thread.__init__(self)
        self.port = port
        self.ip = ip
        self.chain = chain
        self.transaction = transaction

    def run(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.bind((self.ip, self.port))
        soc.listen(1)
        while True:
            (socClient, addrClient) = soc.accept()
            try:
                while True:
                    data = socClient.recv(4096)
                    if data == ''.encode(encoding='Utf-8'):
                        break
                    socClient.sendall(str('ok').encode(encoding='Utf-8'))
                    data = json.loads(data)
                    try:
                        data["block"]
                    except:
                        self.transaction.updatetransaction(data, "ajout")
                    else:
                        self.chain.add_block(data)
                socClient.close()
            except socket.error:
                print('client interrompu')
                break


class Miner(Thread):

    def __init__(self, chain, transaction, ips):
        Thread.__init__(self)
        self.chain = chain
        self.transaction = transaction
        self.ips = ips

    def run(self):
        while True:
            current_transaction = self.transaction.gettransaction()
            self.chain.generate_block(current_transaction)
            bchain = self.chain.blockChain.json.encode('Utf-8')
            for i in self.ips["miner"]:
                port = 7777
                connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                connection.connect((i, port))
                connection.sendall(bchain)
                connection.close()
            for i in self.ips["client"]:
                port = 7777
                connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                connection.connect((i, port))
                connection.sendall(bchain)
                connection.close()


thread_listen = ListenChain(7777, ip, chain, transaction)
thread_miner = Miner(chain, transaction, ips)

thread_listen.start()
thread_miner.start()

thread_listen.join()
thread_miner.join()
