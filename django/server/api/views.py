import json
import logging

from django.http import JsonResponse

from api.models import Address

logger = logging.getLogger(__name__)


def index(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        address = body_data['address']
        addr = Address(address=address)
        addr.save()
        logger.info(f"Address {address} has been added")
    elif request.method == "DELETE":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        address = body_data["address"]
        addr = Address.objects.filter(address=address)
        addr.delete()

        logger.info(f"Address {address} has been deleted")

    results = []

    for addr in Address.objects.all():
        results.append(addr.address)

    logger.info(results)

    return JsonResponse(results, safe=False)
