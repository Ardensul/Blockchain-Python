import json


def read_transaction():
    with open("data.json", "r") as file:
        transaction = json.load(file)
        return transaction


def add_transaction(new_transaction):
    transaction = read_transaction()
    transaction.append({
        "date": new_transaction.date,
        "sender": new_transaction.sender,
        "receive": new_transaction.receive,
        "amount": new_transaction.amount
    })

    with open("data.json", "w") as file:
        json.dump(transaction, file)
