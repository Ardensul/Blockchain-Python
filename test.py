import hashlib

hash_objet = hashlib.sha256(b'coucou')
value = hash_objet.hexdigest()

print(value)