from hashlib import *


class Block:
    def __init__(self, data, prev_hash='genesis', id=0, work_proof=0, current_hash=''):
        self.id = id
        self.previousHash = prev_hash
        self.data = data
        docpre = open("./conf/workproof.conf", "r")
        self.prefix = docpre.readline()
        docpre.close()
        self.workProof = work_proof
        if current_hash != '':
            self.currentHash = current_hash
        else:
            self.currentHash = self._current_hash()

    def verify_hash(self):
        block = str(self.previousHash) + str(self.data) + str(self.workProof)
        block = block.encode(encoding='Utf-8')
        hash_object = sha256(block).hexdigest()
        return hash_object

    def _current_hash(self):
        is_finish = False
        hash_object = ''
        while not is_finish:
            block = str(self.previousHash) + str(self.data) + str(self.workProof)
            block = block.encode(encoding='Utf-8')
            hash_object = sha256(block).hexdigest()
            if hash_object[0:5] != "0000a":
                self.workProof += 1
            else:
                is_finish = True
        return hash_object
