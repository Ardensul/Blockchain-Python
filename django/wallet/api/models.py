from django import forms


class User(forms.Form):
    private_key = forms.CharField(required=True)
    public_key = forms.CharField(required=True)

    def get_unique_key(self):
        return self["public_key"]  # TODO

    def get_amount(self):
        return self["public_key"]  # TODO


class Transaction(forms.Form):
    private_key = forms.CharField(required=True)
    public_key = forms.CharField(required=True)
    sender = forms.CharField(required=True)
    receive = forms.CharField(required=True)
    amount = forms.IntegerField(required=True)

    def to_json(self, user: User):
        return f"privateKey: {user['private_key'].data}, publicKey: {user['public_key'].data}, " \
            f"sender: {self['sender'].data}, receive: {self['receive'].data}, amount: {self['amount'].data}"
