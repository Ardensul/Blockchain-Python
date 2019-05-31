import json
import rsa


class Transaction:
    def __init__(self):
        self.path = "../test/transactions.json"
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

    def veriftransa(self,transa):
        verif = "from: "+str(transa["from"]) + ", to:" + str(transa["to"]) + ",amount: " + str(transa["amount"])
        verif.encode(encoding='Utf-8')
        crypt = rsa.encrypt(verif,transa["privateKey"])
        if crypt == transa["hash"]:
            return True
        else:
            return False

