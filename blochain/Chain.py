from Block import *
import rsa
import os
import json

class Chain:
    def __init__(self):
        self.path = "../test/chain.json"
        self.blockChain = [0]
        exist = os.path.isfile(self.path)
        if exist:
            self.load_chain()
        else:
            if len(self.blockChain) == 1:
                self.blockChain[0] = Block("genesis")
                self.saveChain()

    def generateBlock(self,data):
        block = Block(data,self.blockChain[-1].currentHash,self.blockChain[-1].id+1)
        self.blockChain.append(block)
        self.saveChain()


    def integrity_check(self):
        for i in range(1,len(self.blockChain)):
            if (self.blockChain[i].previousHash == self.blockChain[i-1].verifyhash()) and (self.blockChain[i].verifyhash() == self.blockChain[i].currentHash) :
                continue
            else:
                return False
        return True

    def load_chain(self):
        saveFile = open(self.path,'r')
        data = json.load(saveFile)
        for i in range(len(data["block"])):
            if i == 0:
                self.blockChain[i] = Block(data["block"][i]["data"],data["block"][i]["previousHash"],data["block"][i]["id"],data["block"][i]["workProof"],data["block"][i]["currentHash"])
            else:
                self.blockChain.append(Block(data["block"][i]["data"],data["block"][i]["previousHash"],data["block"][i]["id"],data["block"][i]["workProof"],data["block"][i]["currentHash"]))
        saveFile.close()

    def saveChain(self):
        saveFile = open(self.path,'w')
        data = {}
        data["block"] = []
        for i in range(len(self.blockChain)):
            data["block"].append(self.blockChain[i].__dict__)
        json.dump(data,saveFile)
        saveFile.close()
        return True

    def addBlock(self,data):
        id = len(data["block"])-1
        self.blockChain.append(Block(data["block"][id]["data"], data["block"][id]["previousHash"], data["block"][id]["id"],data["block"][id]["workProof"], data["block"][id]["currentHash"]))

