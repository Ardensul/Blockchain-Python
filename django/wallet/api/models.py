import rsa
from django import forms


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
        # noinspection SpellCheckingInspection
        message = "UUS1D58gipJxeynVyLCs1phzgj7w18nBb8dCLaJM".encode("utf8")
        message_encrypt = rsa.encrypt(message, rsa.PublicKey.load_pkcs1(self["public_key"].data))
        message_decrypt = rsa.decrypt(message_encrypt, rsa.PrivateKey.load_pkcs1(self["private_key"].data))
        return message == message_decrypt

    @staticmethod
    def create_key():
        (public, private) = rsa.newkeys(512)
        return {"public": public.save_pkcs1().decode('utf8'),
                "private": private.save_pkcs1().decode('utf8')}


class Transaction(forms.Form):
    receive = forms.CharField(required=True)
    amount = forms.IntegerField(required=True)

    def to_json(self, user: User):
        return f"publicKey: {user['public_key'].data}, from: TODO, to: {self['receive'].data}, " \
            f"amount: {self['amount'].data}"  # FIXME
