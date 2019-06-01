import hashlib

import rsa
from django import forms
from django.core.validators import RegexValidator


class User(forms.Form):
    """Form and representation of an user"""
    private_key = forms.CharField(required=True, widget=forms.Textarea)
    public_key = forms.CharField(required=True, widget=forms.Textarea)

    def get_private_key(self):
        """Read a private key in PKCS#1 PEM format.

        :return: a PrivateKey object
        """
        return rsa.PrivateKey.load_pkcs1(self["private_key"].data)

    def get_public_key(self):
        """Read a public key in PKCS#1 PEM format.

        :return: a PublicKey object
        """
        return rsa.PublicKey.load_pkcs1(self["public_key"].data)

    def get_unique_key(self):  # FIXME
        key = self._sha256(self["public_key"].data)
        key_ripemd160 = self._ripemd160(key)
        key = self._sha256(key_ripemd160)
        key = self._sha256(key)
        key = key_ripemd160 + key[0:4]
        key = self._md5(key)
        return key

    def get_amount(self):
        return self["public_key"]  # TODO

    def check_key(self):
        """Verifies that the public key and the private key match.

        :return: a boolean, true if they match otherwise false
        """
        # noinspection PyBroadException
        try:
            # noinspection SpellCheckingInspection
            message = "UUS1D58gipJxeynVyLCs1phzgj7w18nBb8dCLaJM".encode("utf8")
            message_encrypt = rsa.encrypt(message, self.get_public_key())
            message_decrypt = rsa.decrypt(message_encrypt, self.get_private_key())
            return message == message_decrypt
        except:
            return False

    def export(self):
        """Returns the public and private key.

        :return: a dictionary
        """
        return {"public_key": self["public_key"].data, "private_key": self["private_key"].data}

    @staticmethod
    def create_key():
        """Generates new public and private keys

        :return: a dictionary
        """
        (public, private) = rsa.newkeys(512)
        return {"public": public.save_pkcs1().decode('utf8'),
                "private": private.save_pkcs1().decode('utf8')}

    @staticmethod
    def _sha256(message):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(message.encode("utf-8"))
        return sha256_hash.hexdigest()

    @staticmethod
    def _md5(message):
        md5_hash = hashlib.md5()
        md5_hash.update(message.encode("utf-8"))
        return md5_hash.hexdigest()

    @staticmethod
    def _ripemd160(message):
        ripemd160_hash = hashlib.new("ripemd160")
        ripemd160_hash.update(message.encode("utf-8"))
        return ripemd160_hash.hexdigest()


class Transaction(forms.Form):
    """Form and representation of a transaction."""
    receive = forms.CharField(required=True)
    amount = forms.IntegerField(required=True)

    def export(self, user: User):
        """Returns the transaction with the signature.

        :param user: the :py:class:`User` to complete and sign the transaction
        :return: a string representing the transaction
        """
        message = f"from: {user.get_unique_key()}, to: {self['receive'].data}, amount: {self['amount'].data}"
        message_signature = rsa.sign(message.encode("utf8"), user.get_private_key(), "SHA-256")
        # TODO: change hast to sign/signature ?
        return f"privateKey: {user['private_key'].data}, " + message + f", hash: {message_signature}"


class BankTransfer(forms.Form):
    """Form and representation of a bank transfer."""
    IBAN = forms.CharField(required=True, max_length=33,
                           validators=[RegexValidator(r'[A-Z]{2}[0-9]{2}\s([0-9]{4}\s){5}[0-9]{3}', "not an IBAN")])
    BIC = forms.CharField(required=True, max_length=12)
    amount = forms.IntegerField(required=True)
