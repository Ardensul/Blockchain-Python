from django.shortcuts import render, redirect

from api.models import Transaction, User, PayingCard


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
    transaction_from = Transaction(None)
    card_form = PayingCard(request.POST or None)
    return render(request, 'transaction.html', {"login": True}, locals())
