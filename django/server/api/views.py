import json
import logging

from django.db import IntegrityError
from django.http import JsonResponse

from api.models import Miner, Client

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

        try:
            miner_address = body_data['miner']
            miner = Miner(address=miner_address)
            miner.save()
            logger.info(f"Address {miner_address} has been added")
        except (KeyError, IntegrityError):
            pass

        try:
            client_address = body_data['client']
            client = Client(address=client_address)
            client.save()
            logger.info(f"Address {client_address} has been added")
        except (KeyError, IntegrityError):
            pass

    elif request.method == "DELETE":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        try:
            minor_address = body_data["miner"]
            minor = Miner.objects.filter(address=minor_address)
            minor.delete()
            logger.info(f"Address {minor_address} has been deleted")
        except KeyError:
            pass

        try:
            client_address = body_data["client"]
            client = Client.objects.filter(address=client_address)
            client.delete()
            logger.info(f"Address {client_address} has been deleted")
        except KeyError:
            pass

    miner_results = []
    client_results = []

    for miner in Miner.objects.all():
        miner_results.append(miner.address)

    for client in Client.objects.all():
        client_results.append(client.address)

    results = {"miner": miner_results, "client": client_results}

    logger.info(results)

    return JsonResponse(results, safe=False)
