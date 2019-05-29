import rsa
from django import forms
from django.core.validators import RegexValidator


class User(forms.Form):
    private_key = forms.CharField(required=True, widget=forms.Textarea)
    public_key = forms.CharField(required=True, widget=forms.Textarea)

    def get_private_key(self):
        return rsa.PrivateKey.load_pkcs1(self["private_key"].data)

    def get_public_key(self):
        return rsa.PublicKey.load_pkcs1(self["public_key"].data)

    def get_unique_key(self):
        return self["public_key"]  # TODO

    def get_amount(self):
        return self["public_key"]  # TODO

    def check_key(self):
        # noinspection PyBroadException
        try:
            # noinspection SpellCheckingInspection
            message = "UUS1D58gipJxeynVyLCs1phzgj7w18nBb8dCLaJM".encode("utf8")
            message_encrypt = rsa.encrypt(message, rsa.PublicKey.load_pkcs1(self["public_key"].data))
            message_decrypt = rsa.decrypt(message_encrypt, rsa.PrivateKey.load_pkcs1(self["private_key"].data))
            return message == message_decrypt
        except:
            return False

    def export(self):
        return {"public_key": self["public_key"].data, "private_key": self["private_key"].data}

    @staticmethod
    def create_key():
        (public, private) = rsa.newkeys(512)
        return {"public": public.save_pkcs1().decode('utf8'),
                "private": private.save_pkcs1().decode('utf8')}


class Transaction(forms.Form):
    receive = forms.CharField(required=True)
    amount = forms.IntegerField(required=True)

    def to_json(self, user: User):
        message = f"from: {user.get_unique_key()}, to: {self['receive'].data}, amount: {self['amount'].data}"
        hash_message = rsa.encrypt(message.encode("utf8"), user.get_public_key())
        return f"privateKey: {user['private_key'].data}, " + message + f", hash: {hash_message}"


class PayingCard(forms.Form):
    IBAN = forms.CharField(required=True, max_length=33,
                           validators=[RegexValidator(r'[A-Z]{2}[0-9]{2}\s([0-9]{4}\s){5}[0-9]{3}', "not an IBAN")])
    BIC = forms.CharField(required=True, max_length=12)
    amount = forms.IntegerField(required=True)
