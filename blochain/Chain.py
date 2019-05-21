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

    def generateBlock(self,data):
        block = Block(data,self.blockChain[-1].currentHash,self.blockChain[-1].id+1)
        self.blockChain.append(block)
        self.saveChain()

    def data_check(self,data):
        if not data.emeteur or not data.receveur or not data.montant or not data.publicKey or not data.signature:
            return False
        txt = str(data.emeteur)+str(data.receveur)+str(data.montant)
        decod = rsa.decrypt(data.signature,data.publicKey)
        if txt != decod:
            return False
        return True

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

    def saveChain(self):
        saveFile = open(self.path,'w')
        data = {}
        data["block"] = []
        for i in range(len(self.blockChain)):
            data["block"].append(self.blockChain[i].__dict__)
        json.dump(data,saveFile)
        return True
