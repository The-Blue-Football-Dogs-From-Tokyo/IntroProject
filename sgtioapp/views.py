from django.core.management.base import NoArgsCommand
from django.shortcuts import render_to_response
import requests
import logging
logger = logging.getLogger(__name__)
def sgtio_template(request):

        product = request.GET.get("search")
        logger.debug("User searched for " + product)
        url = "https://api.sgt.io/products/?api_key=4c4ec8961617eee94e2469b1fea9f5587d64b6d3&q=" + product + "&format=json"

        r = requests.get(url)
        products = {"products":r.json()}
	return render_to_response('template.html',products)

