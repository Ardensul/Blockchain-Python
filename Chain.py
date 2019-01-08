from Block import *

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


test = Chain()

for i in range(15):
    test.generateBlock(i)

for i in range(len(test.blockChain)):
    print(test.blockChain[i].__dict__)

