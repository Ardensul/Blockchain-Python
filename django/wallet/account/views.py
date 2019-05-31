from django.shortcuts import render, redirect

from account.models import Transaction, User, PayingCard
from account.utils import get_company_account


def index(request):  # TODO
    return render(request, 'form.html', {"login": True})


def login(request):
    """View of the login page.

    :param request: Object containing the web request
    :return: a render whose content contains a from template
    """
    form = User(request.POST or None)
    if form.is_valid():
        if form.check_key():
            u = form.export()
            print(u, u["private_key"])
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
    print(key)
    return render(request, 'form.html')  # TODO


def transaction(request):
    """View allowing the user to create a transaction or convert money to cryptomonnaise.

    :param request: Object containing the web request
    :return: a render whose content contains a transaction template
    """
    transaction_form = Transaction(None)
    card_form = PayingCard(None)

    # noinspection PyShadowingNames
    login = True
    return render(request, 'transaction.html', locals())


def send_transaction(request):
    if request.method == "POST":
        transaction_form = Transaction(request.POST)

        if transaction_form.is_valid():
            user = User(request.session["user"])
            print("TODO")  # TODO: send transaction to miner
    else:
        return redirect("transaction")


def send_payment(request):
    if request.method == "POST":
        payment_form = PayingCard(request.POST)

        if payment_form.is_valid():
            user = User(request.session["user"])
            company = get_company_account()
            print("TODO")  # TODO: create payment
    else:
        return redirect("transaction")
