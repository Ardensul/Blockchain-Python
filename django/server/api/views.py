import json

from django.http import JsonResponse
from api.models import Address


def index(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        address = Address(address=body_data['address'])
        address.save()

        return JsonResponse({"success": True})
    else:
        results = []
        for addr in Address.objects.all():

            print(addr.address)
            results.append(addr.address)

        print(results)

        return JsonResponse(results, safe=False)
