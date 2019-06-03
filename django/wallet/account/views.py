from django.shortcuts import render, redirect

from account.models import Transaction, User, BankTransfer, Network
from account.utils import get_company_account


def index(request):  # TODO
    user = User(request.session["user"])
    user_address = user.get_unique_key()
    return render(request, 'wallet.html', {"login": True, "user_address": user_address})


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
    :return: a render whose content contains a *** template TODO
    """
    key = User.create_key()
    return render(request, 'login')  # TODO


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
                payment_transfer = Transaction({"beneficiary": user.get_unique_key(),
                                                "amount": payment_form["amount"].data})
                success = Network().send(payment_transfer.export(company))
                request.session["send_payment"] = success
            else:
                request.session["send_payment"] = False
        else:
            request.session["send_payment"] = False

    return redirect("transaction")
