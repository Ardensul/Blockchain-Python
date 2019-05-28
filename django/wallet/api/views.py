from django.shortcuts import render, redirect
from django.utils import timezone

from api.models import Transaction, User
from api.utils import middleware_login


def index(request):
    print(timezone.now())
    return render(request, "test.html")


def login(request):
    if middleware_login(request):
        return redirect("/api/")

    middleware_login(request)
    router = "login"
    form = User(request.POST or None)
    if form.is_valid():
        if form.check_key():
            request.session["user"] = "o"  # FIXME
            return redirect("/api/")
    return render(request, 'transaction.html', locals())


def send_from(request):
    if not middleware_login(request):
        return redirect("/api/login")

    router = "form"
    form = Transaction(request.POST or None)
    if form.is_valid():
        send = True
        # results = transaction.to_json()
        # TODO: send transaction to blockchain

    return render(request, 'transaction.html', locals())
