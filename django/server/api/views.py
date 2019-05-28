import json

from django.http import JsonResponse

from api.models import Address


def index(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        addr = Address(address=body_data['address'])
        addr.save()
    elif request.method == "DELETE":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        addr = Address.objects.filter(address=body_data["address"])
        addr.delete()

    results = []
    for addr in Address.objects.all():
        print(addr.address)
        results.append(addr.address)

    print(results)

    return JsonResponse(results, safe=False)
