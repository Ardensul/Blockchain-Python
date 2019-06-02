import json
import logging

from django.http import JsonResponse

from api.models import Address

logger = logging.getLogger(__name__)


def index(request):
    """Processes requests on the API.
    If it is a POST request, it will add the address contained in parameter in its list.
    If it is a DELETE request, it will delete the address contained in the parameter from its list.

    :param request: Object containing the web request
    :return: a JSON response containing the available address list
    """
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
