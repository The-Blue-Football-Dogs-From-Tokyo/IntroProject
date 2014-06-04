from django.conf import settings
from django.shortcuts import render
from django.core.management.base import NoArgsCommand
from django.template import Context, Template
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.

def get_json_object(json):
	return json

def sgtio_template(request):
	
	
	c = {"products":
			[{
        		"title": "Apple iPhone 3G - 8GB - Black (Unlocked) Smartphone New", 
        		"price": "119.95", 
        		"description": "fresca", 
        		"merchant": "eBay", 
        		"url": "http://api.socialingot.com/click/widget/?afsrc=1&key=208277&deal=467287&url=http://www.ebay.com/itm/Apple-iPhone-3G-8GB-Black-Unlocked-Smartphone-New-/161280045139?pt=Cell_Phones", 
        		"shipping_cost": "0.00", 
        		"currency_code": "USD", 
        		"image_url": "http://thumbs4.ebaystatic.com/m/mhRaAtxUwQ_ttPUq3Zac3qg/140.jpg"
   		},
		{
			"title": "? Apple iPHONE 3GS - 8GB BLACK - (Factory Unlocked) SmartPhone Cell Phone", 
        		"price": "119.95", 
        		"description": "no descrip", 
        		"merchant": "eBay", 
        		"url": "http://api.socialingot.com/click/widget/?afsrc=1&key=208277&deal=467287&url=http://www.ebay.com/itm/Apple-iPHONE-3GS-8GB-BLACK-Factory-Unlocked-SmartPhone-Cell-Phone-/151317976431?pt=Cell_Phones", 
        		"shipping_cost": "0.00", 
        		"currency_code": "USD", 
        		"image_url": "http://thumbs4.ebaystatic.com/m/mAg_WtIkLw4PMAQGdMV5MrA/140.jpg"
			}]
		}
		

	
	#f = open('write_test.txt', 'w')
	#f.write(t.render(c))
	#f.close

	return render_to_response('template.html', c)

