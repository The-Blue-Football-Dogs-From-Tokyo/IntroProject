from django.core.management.base import NoArgsCommand
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
import requests
import logging
logger = logging.getLogger(__name__)
def sgtio_template(request):

    product = request.GET.get("search")
    
    if product == 'pong':
        return redirect("http://www.stevelange.net/flash/pong02.swf")
        
    if product is not None:
        logger.debug("User searched for " + product)
        url = "https://api.sgt.io/products/?api_key=4c4ec8961617eee94e2469b1fea9f5587d64b6d3&q=" + product + "&format=json"
        r = requests.get(url)
        products = {"products":r.json()}
        return render_to_response('template.html',products)
    else:
        return render_to_response('template.html')
