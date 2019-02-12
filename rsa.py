from math import *
from random import *

class Rsa:

    @staticmethod
    def genClef():
        clefs = {"privée": (0, 0), "publique": (0, 0)}
        p = randint(10000,100000)
        q = randint(10000,100000)
        #verifiaction que p et q soient premiers et non égaux
        finish = False
        while not finish:
            verifOk = True
            for i in range(2,int(abs(sqrt(p))+1)):
                if p%i == 0:
                    p = randint(10000,100000)
                    verifOk = False
                    break
                else:
                    continue
            if verifOk:
                finish = True
        finish = False
        while not finish:
            verifOk = True
            if q == p :
                q = randint(10000, 100000)
            for i in range(2,int(abs(sqrt(q))+1)):
                if q%i == 0:
                    q = randint(10000,100000)
                    verifOk = False
                    break
                else:
                    continue
            if verifOk:
                finish = True
        print(p,q)
        n = p*q
        totien = (p-1)*(q-1)
        print(totien)
        e = randint(100,1000)
        while(gcd(e,totien) !=1):
            e = randint(1,1000)
        if(p < q):
            d = q
        else:
            d = p
        compteur = 0
        while compteur == 0:
            # Les conditions vues ci-dessus :
            if ((e * d % totien == 1) and (p < d) and (q < d) and (d < totien)):
                compteur = 1
            d = d + 1
            print(d)
        d = d - 1


        clefs = {"publique": (n, e), "privée": (n, d)}

        return clefs

    @staticmethod
    def encrypt(n, e, data):
        crypt = (data**e) % n
        return crypt

    @staticmethod
    def decrypt(n,d,data):
        decrypt = (data**d) % n
        return decrypt

clef = Rsa.genClef()
donnee = 18
crypte = Rsa.encrypt(clef["publique"][0],clef["publique"][1],donnee)
decrypte = Rsa.decrypt(clef["privée"][0],clef["privée"][1],crypte)

print(clef)
print(clef["publique"][0])
print(donnee)
print(crypte)
print(decrypte)