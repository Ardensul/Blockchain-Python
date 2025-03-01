import json

from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from account.models import Transaction, User, BankTransfer, Network, SaveTransaction
from account.utils import get_company_account


def index(request):
    user = User(request.session["user"])
    user_address = user.get_address()
    user_amount = user.get_amount()
    return render(request, 'wallet.html', {"login": True, "user_address": user_address, "user_amount": user_amount})


def login(request):
    """View of the login page.

    :param request: Object containing the web request
    :return: a render whose content contains a from template
    """
    form = User(request.POST or None)
    if form.is_valid():
        if form.check_key():
            u = form.export()
            request.session["user"] = form.export()
            return redirect("/")
    input_message = "Log in"
    return render(request, 'login.html', locals())


def logout(request):
    """View to disconnect the user.

    :param request: Object containing the web request
    :return: a redirection to the index
    """
    try:
        del request.session["user"]
    finally:
        return redirect('/')


def new_key(request):
    """View generating new RSA keys

    :param request: Object containing the web request
    :return: a render whose content contains a new_keys.html template
    """
    key = User.create_key()
    return render(request, 'new_keys.html', {"public_key": key["public"], "private_key": key["private"]})


def transaction(request):
    """View allowing the user to create a transaction or convert money to cryptomonnaise.

    :param request: Object containing the web request
    :return: a render whose content contains a transaction template
    """
    transaction_form = Transaction(None)
    bank_form = BankTransfer(None)

    send_transaction_success = None
    send_payment_success = None

    try:
        send_transaction_success = request.session["send_transaction"]
        del request.session["send_transaction"]
    except KeyError:
        pass

    try:
        send_payment_success = request.session["send_payment"]
        del request.session["send_transaction"]
    except KeyError:
        pass

    # noinspection PyShadowingNames
    login = True
    return render(request, 'transaction.html', locals())


def send_transaction(request):
    if request.method == "POST":
        transaction_form = Transaction(request.POST)

        if transaction_form.is_valid():
            user = User(request.session["user"])
            if user.get_amount() >= int(transaction_form["amount"].data):
                success = Network().send(transaction_form.export(user))
                request.session["send_transaction"] = success
            else:
                request.session["send_transaction"] = False
        else:
            request.session["send_transaction"] = False

    return redirect("transaction")


def send_payment(request):
    if request.method == "POST":
        payment_form = BankTransfer(request.POST)

        if payment_form.is_valid():
            user = User(request.session["user"])
            company = get_company_account()
            if company.get_amount() >= int(payment_form["amount"].data):
                payment_transfer = Transaction({"beneficiary": user.get_address(),
                                                "amount": payment_form["amount"].data})
                success = Network().send(payment_transfer.export(company))
                request.session["send_payment"] = success
            else:
                request.session["send_payment"] = False
        else:
            request.session["send_payment"] = False

    return redirect("transaction")


def save_transaction(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        data = body_data["data"]

        block_transaction = SaveTransaction(sender=data["from"], receive=data["to"], amount=data["amount"],
                                            timestamp=data["timestamp"], signature=data["signature"])
        try:
            block_transaction.save()
        except IntegrityError:
            pass

    return HttpResponse(status=200)
