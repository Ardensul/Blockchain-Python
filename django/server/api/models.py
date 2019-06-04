from django.db import models


class Minor(models.Model):
    """Model representing the Address table in the database"""
    address = models.TextField(unique=True)

    def __str__(self):
        return self.address


class Client(models.Model):
    """Model representing the Address table in the database"""
    address = models.TextField(unique=True)

    def __str__(self):
        return self.address
