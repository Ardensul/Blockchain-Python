from django import forms
from django.db import models
from django.utils import timezone


class Transaction(forms.Form):
    private_key = forms.CharField(required=True)
    public_key = forms.CharField(required=True)
    sender = forms.CharField(required=True)
    receive = forms.CharField(required=True)
    amount = forms.IntegerField(required=True)

    def to_json(self):
        return {"privateKey": self["private_key"].data, "publicKey": self["public_key"].data,
                "sender": self["sender"].data, "receive": self["receive"].data, "amount": self["amount"].data,
                "date": str(timezone.now())}


class User(models.Model):
    private_key = models.TextField("private_key")
    public_key = models.TextField("public_key")
    balance = models.FloatField("balance")
