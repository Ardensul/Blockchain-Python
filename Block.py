from hashlib import *

class Block:
    def __init__(self, data, prevhash = ''):
        self.previousHash = '123456789'
        self.data = data
        self.signatur = 'RS'
        self.workProof = 0
        self.currentHash = self.currenthash()

    def currenthash(self):
        isfinish = False
        hash_objet = ''
        while not isfinish :
            block = str(self.previousHash) + str(self.data) + str(self.signatur) + str(self.workProof)
            block = block.encode(encoding='Utf-8')
            hash_objet = sha256(block).hexdigest()
            if hash_objet[0:5] != "0000a":
                print(str(self.workProof) + " Pas bon comme hash : " + hash_objet)
                self.workProof += 1
            else:
                isfinish = True
                print("Bien évidemment la solution était : " + hash_objet)
        return hash_objet


test = Block('Bonjour')

print(test.__dict__)