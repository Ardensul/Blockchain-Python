import os

from django.conf import settings

from account.models import User


# noinspection PyUnresolvedReferences
def get_company_account():
    path = settings.NAME_COMPANY_KEY_FILES
    private_path = os.path.join(os.path.dirname(__file__), f"../data/{path}")
    public_path = os.path.join(os.path.dirname(__file__), f"../data/{path}.pub")

    with open(public_path, mode='rb') as public_file:
        public_key = public_file.read()

    with open(private_path, mode='rb') as private_file:
        private_key = private_file.read()

    keys = {"public_key": public_key.decode("utf8"), "private_key": private_key.decode("utf8")}

    return User(keys)
