from re import *
from hashlib import *
from random import *

test = ""

for i in range(0,100):
    test = test + str(randint(0,9))

print(test)
test = test.encode('Utf-8')

htest = sha256(test).hexdigest()
print(htest[0:2])
