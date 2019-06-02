from django.db import models


class Address(models.Model):
    """Model representing the Address table in the database"""
    address = models.TextField()

    def __str__(self):
        return self.address
