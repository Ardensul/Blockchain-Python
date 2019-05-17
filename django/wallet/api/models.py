from django.db import models

class Transaction(models.Model):
    date = models.DateField("date")
    sender = models.CharField("sender")
    receive = models.CharField("receive")
    amount = models.IntegerField("amount")
