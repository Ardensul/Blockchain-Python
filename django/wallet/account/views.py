from django.shortcuts import render, redirect

from account.models import Transaction, User, BankTransfer
from account.utils import get_company_account


def index(request):  # TODO
    return render(request, 'wallet.html', {"login": True})


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
    return render(request, 'form.html', locals())


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
    :return: a render whose content contains a *** template TODO
    """
    key = User.create_key()
    return render(request, 'form.html')  # TODO


def transaction(request):
    """View allowing the user to create a transaction or convert money to cryptomonnaise.

    :param request: Object containing the web request
    :return: a render whose content contains a transaction template
    """
    transaction_form = Transaction(None)
    bank_form = BankTransfer(None)

    try:
        send_transaction_success = request.session["send_transaction"]
        del request.session["send_transaction"]
    except:
        print("no transaction")

    try:
        send_payment_success = request.session["send_payment"]
        del request.session["send_transaction"]
    except:
        print("no payment")

    # noinspection PyShadowingNames
    login = True
    return render(request, 'transaction.html', locals())


def send_transaction(request):
    if request.method == "POST":
        transaction_form = Transaction(request.POST)

        if transaction_form.is_valid():
            user = User(request.session["user"])
            print("TODO")  # TODO: send transaction to miner
            request.session["send_transaction"] = True
        else:
            request.session["send_transaction"] = False

    return redirect("transaction")


def send_payment(request):
    if request.method == "POST":
        payment_form = BankTransfer(request.POST)

        if payment_form.is_valid():
            user = User(request.session["user"])
            company = get_company_account()
            print("TODO")  # TODO: create payment
            request.session["send_payment"] = True
        else:
            request.session["send_payment"] = False

    return redirect("transaction")
