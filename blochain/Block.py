from hashlib import *


class Block:
    def __init__(self, data, prevhash = 'genesis',id = 0,workProof=0,currentHash=''):
        self.id = id
        self.previousHash = prevhash
        self.data = data
        docpre = open("./conf/workproof.conf","r")
        self.prefix = docpre.readline()
        docpre.close()
        self.workProof = workProof
        if currentHash != '':
            self.currentHash = currentHash
        else:
            self.currentHash = self.currenthash()

    def currenthash(self):
        isfinish = False
        hash_objet = ''
        while not isfinish :
            block = str(self.previousHash) + str(self.data) + str(self.workProof)
            block = block.encode(encoding='Utf-8')
            hash_objet = sha256(block).hexdigest()
            if hash_objet[0:5] != "0000a":
                self.workProof += 1
            else:
                isfinish = True
        return hash_objet


    def verifyhash(self):
        block = str(self.previousHash) + str(self.data) + str(self.workProof)
        block = block.encode(encoding='Utf-8')
        hash_objet = sha256(block).hexdigest()
        return hash_objet

