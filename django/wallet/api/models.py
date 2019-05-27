from django import forms


class Transaction(forms.Form):
    private_key = forms.CharField(required=True)
    public_key = forms.CharField(required=True)
    sender = forms.CharField(required=True)
    receive = forms.CharField(required=True)
    amount = forms.IntegerField(required=True)

    def to_json(self):
        return "privateKey: ${self['private_key'].data}, publicKey: {self['public_key'].data}, sender: {self[" \
               "'sender'].data}, receive: {self['receive'].data}, amount: {self['amount'].data} "


class User(forms.Form):
    private_key = forms.CharField(required=True)
    public_key = forms.CharField(required=True)

    def get_unique_key(self):
        return self["public_key"]  # TODO

    def get_amount(self):
        return self["public_key"]  # TODO
