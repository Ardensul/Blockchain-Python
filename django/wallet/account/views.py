from django.shortcuts import render, redirect

from account.models import Transaction, User, PayingCard


def index(request):
    return render(request, 'form.html', {"login": True})


def login(request):
    form = User(request.POST or None)
    if form.is_valid():
        if form.check_key():
            request.session["user"] = form.export()
            return redirect("/")
    return render(request, 'form.html', locals())


def logout(request):
    try:
        del request.session["user"]
    finally:
        return redirect('/')


def transaction(request):
    transaction_form = Transaction(None)
    card_form = PayingCard(None)

    # noinspection PyShadowingNames
    login = True
    return render(request, 'transaction.html', locals())


def send_transaction(request):
    if request.method == "POST":
        transaction_form = Transaction(request.POST)

        if transaction_form.is_valid():  # TODO: send transaction to miner
            user = User(request.session["user"])
            print()
    else:
        return redirect("transaction")


def send_payment(request):
    if request.method == "POST":
        payment_form = PayingCard(request.POST)

        if payment_form.is_valid():  # TODO: create payment
            user = User(request.session["user"])
            print()
    else:
        return redirect("transaction")
