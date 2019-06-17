import json
import socket
from threading import Thread

import requests

from blochain.Chain import Chain
from blochain.Transcation import Transaction

web_directory_host = "http://127.0.0.1:8000/"

ip = ""

try:
    ip = requests.get('https://api.ipify.org').text
except:
    print("Connection error with api.ipify.org")
    exit()

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
                        self.transaction.update_transaction(data, "ajout")
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
            current_transaction = self.transaction.get_transaction()
            if current_transaction :
                self.chain.generate_block(current_transaction)
                bchain = self.chain.blockChain.json.encode('Utf-8')
                for i in self.ips["miner"]:
                    port = 7777
                    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                    try:
                        connection.connect((i, port))
                        connection.sendall(bchain)
                    except socket.error:
                        data = json.dumps({"miner": i})
                        try:
                            requests.delete(web_directory_host, data=data)
                        except:
                            pass
                    finally:
                        connection.close()

                for i in self.ips["client"]:
                    try:
                        requests.post(i, bchain)
                    except:
                        pass


try:
    ips = requests.get(web_directory_host)

    thread_listen = ListenChain(7777, ip, chain, transaction)
    thread_miner = Miner(chain, transaction, ips.json())

    thread_listen.start()
    thread_miner.start()

    thread_listen.join()
    thread_miner.join()

except:
    print("Connection error with the web directory host")
    exit()
