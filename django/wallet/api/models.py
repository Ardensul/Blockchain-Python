from django.db import models

class Transaction(models.Model):
    date = models.DateField("date")
    sender = models.TextField("sender")
    receive = models.TextField("receive")
    amount = models.IntegerField("amount")

class User(models.Model):
    private_key = models.TextField("private_key")
    public_key = models.TextField("public_key")
    balance = models.FloatField("balance")
