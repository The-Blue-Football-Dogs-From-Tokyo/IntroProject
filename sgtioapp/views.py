from django.conf import settings
from django.shortcuts import render
from django.core.management.base import NoArgsCommand
from django.template import Context, Template
from django.http import HttpResponse
from django.shortcuts import render_to_response
import requests
# Create your views here.

def sgtio_new(request):
	return

def sgtio_template(request):
        product = request.GET.get("search")

        url = "https://api.sgt.io/products/?api_key=4c4ec8961617eee94e2469b1fea9f5587d64b6d3&q=" + product + "&format=json"

        r = requests.get(url)

	return render_to_response('template.html', )

