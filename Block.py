import hashlib
import json

class Block:
    def __init__(self, data, prevhash = ''):
        self.previousHash = '123456789'
        self.data = data
        self.signatur = 'RS'
        self.workProof = ''
        self.currentHash = self.currenthash()

    def currenthash(self):
        block = str(self.previousHash) + str(self.data) + str(self.signatur) + str(self.workProof)
        block = block.encode(encoding='Utf-8')
        hash_objet = hashlib.sha256(block).hexdigest()
        return hash_objet


test = Block('1')

print(test.__dict__)
