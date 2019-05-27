from django.shortcuts import render
from django.utils import timezone

from api.models import Transaction


def index(request):
    print(timezone.now())
    return render(request, "test.html")


def send_from(request):
    transaction = Transaction(request.POST or None)
    if transaction.is_valid():
        send = True
        results = transaction.to_json()
        # TODO: send transaction to blockchain

    return render(request, 'transaction.html', locals())
