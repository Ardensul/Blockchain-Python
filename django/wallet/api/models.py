from django import forms
from django.db import models
from django.utils import timezone


class Transaction(forms.Form):
    sender = forms.CharField(required=True)
    receive = forms.CharField(required=True)
    amount = forms.IntegerField(required=True)


class User(models.Model):
    private_key = models.TextField("private_key")
    public_key = models.TextField("public_key")
    balance = models.FloatField("balance")
