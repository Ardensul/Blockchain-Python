import hashlib
import json

class Block:
    def __init__(self, data, prevhash = ''):
        self.previousHash = '123456789'
        self.data = data
        self.signatur = 'RS'
        self.workProof = ''
        #self.currentHash = self.currenthash()
        self.block = str(self.previousHash) + str(self.data) + str(self.signatur) + str(self.workProof)

    def currenthash(self):
        block = str(self.previousHash) + str(self.data) + str(self.signatur) + str(self.workProof)
        block.encode(encoding='Bytes')
        #hash_objet = hashlib.sha256(block)
        #value =  hash_objet.hexdigest()
        #return value


test = Block('1')

print(test.block)