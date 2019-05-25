from django.shortcuts import render
from django.utils import timezone

from api.models import Transaction


def index(request):
    print(timezone.now())
    return render(request, "test.html")


def send_from(request):
    transaction = Transaction(request.POST or None)

    if transaction.is_valid():
        # TODO: send transaction to blockchain
        send = True

    return render(request, 'test_from.html', locals())
