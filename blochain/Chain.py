from Block import *
import rsa

class Chain:
    def __init__(self):
        self.blockChain = [1]
        if len(self.blockChain) == 1:
            self.blockChain[0] = Block('genesis')

    def addBlock(self,block):
        self.blockChain.append(block)

    def generateBlock(self,data):
        block = Block(data,self.blockChain[-1].currentHash)
        self.blockChain.append(block)

    def data_check(self,data):
        if not data.emeteur or not data.receveur or not data.montant or not data.publicKey or not data.signature:
            return False
        txt = str(data.emeteur)+str(data.receveur)+str(data.montant)
        decod = rsa.decrypt(data.signature,data.publicKey)
        if txt != decod:
            return False
        return True


test = Chain()

for i in range(5):
    test.generateBlock(i)

for i in range(len(test.blockChain)):
    print(test.blockChain[i].__dict__)

