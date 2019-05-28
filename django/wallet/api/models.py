import rsa
from django import forms


class User(forms.Form):
    private_key = forms.CharField(required=True, widget=forms.Textarea)
    public_key = forms.CharField(required=True, widget=forms.Textarea)

    def get_private_key(self):
        return rsa.PrivateKey.load_pkcs1(self.private_key)  # FIXME

    def get_public_key(self):
        return rsa.PublicKey.load_pkcs1(self.public_key)  # FIXME

    def get_unique_key(self):
        return self["public_key"]  # TODO

    def get_amount(self):
        return self["public_key"]  # TODO

    @staticmethod
    def create_new_user():
        (public, private) = rsa.newkeys(512)
        return {"public": public.save_pkcs1().decode('ascii'),
                "private": private.save_pkcs1().decode('ascii')}


class Transaction(forms.Form):
    private_key = forms.CharField(required=True)
    public_key = forms.CharField(required=True)
    sender = forms.CharField(required=True)
    receive = forms.CharField(required=True)
    amount = forms.IntegerField(required=True)

    def to_json(self, user: User):
        return f"privateKey: {user['private_key'].data}, publicKey: {user['public_key'].data}, " \
            f"sender: {self['sender'].data}, receive: {self['receive'].data}, amount: {self['amount'].data}"
