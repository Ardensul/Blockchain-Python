from Chain import *
from Transaction import *
from threading import Thread
import socket
from requests import get
import json

ip = get('https://api.ipify.org').text
chain = Chain()
transaction = Transaction()

class EcouteChain(Thread):

    def __init__(self, port,ip,chain,transaction):
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
                    if data == ('').encode(encoding='Utf-8'):
                        break
                    socClient.sendall(str('ok').encode(encoding='Utf-8'))
                    data = json.loads(data)
                    try :
                        data["block"]
                    except:
                        self.transaction.updatetransaction(data,"ajout")
                    else:
                        self.chain.addBlock(data)
                socClient.close()
            except socket.error:
                print('client interrompu')
                break

class Mineur(Thread)

    def __init__(self,chain,transaction,ips):
        self.chain = chain
        self.transaction = transaction
        self.ips = ips

    def run(self):
        while True:
            currenttransaction = self.transaction.gettransaction()
            self.chain.generateBlock(currenttransaction)
            bchain = self.chain.blockChain.json.encode('Utf-8')
            for i in self.ips["miner"]:
                port = 7777
                connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                connection.connect((i,port))
                connection.sendall(bchain)
                connection.close()
            for i in self.ips["client"]:
                port = 7777
                connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                connection.connect((i, port))
                connection.sendall(bchain)
                connection.close()


thread_ecoute = EcouteChain(7777,ip,chain,transaction)
thread_mineur = Mineur(chain,transaction,ips)

thread_ecoute.start()
thread_mineur.start()

thread_ecoute.join()
thread_mineur.join()
