import base64
import json
import rsa


class Transaction:
    def __init__(self):
        self.path = "./conf/transactions.json"
        file = open(self.path,'r')
        data = json.load(file)
        self.transaction = []
        for i in range(len(data["transaction"])):
            transa = {
                "from": data["transaction"][i]["from"],
                "to" : data["transaction"][i]["to"],
                "amount" : data["amount"][i]["amount"],
                "privateKey" : data["privateKey"][i]["privateKey"],
                "hash" : data["privateKey"][i]["hash"]
            }
            self.transaction.append(transa)

    def gettransaction(self):
        trans = self.transaction[0]
        self.transaction.pop(0)
        return trans

    def updatetransaction(self,transa,type):
        if type == "ajout":
            self.transaction.append(transa)
        if type == "delet":
            for i in range(len(self.transaction)):
                if transa["hash"] == self.transaction[i]["hash"]:
                    self.transaction.pop(i)
                else:
                    continue

    def veriftransa(self,transac):
        data = {"from": transac["from"], "to": transac["to"], "amount": transac["amount"],
                "publicKey": transac["publicKey"]}
        veryf = base64.b64decode(transac["signature"].encode())
        clef = rsa.PublicKey.load_pkcs1(transac["publicKey"])
        return rsa.verify(str(data).encode(), veryf, clef)

