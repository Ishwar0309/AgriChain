import json
from django.shortcuts import render
from django.contrib import auth 
from django.http import JsonResponse
import pyrebase
from user import views

database = views.database
# print(database.child('user').child('Farmer').child('yields').child(request.session['uid']).get())

def map_analyse(request):
	post_id = request.GET.get('post_id')
	# print(database)
	# sess = request.session['uid']
	# print(sess)
	if post_id == 'my_map':
		# data = {'HI':"Hello"}
		my_data = database.child('user').child('Farmer').child('yields').get()
		# print(my_data)
		main_dict = {}
		
		latitude = []
		longitude = []
		for farmer_key in my_data.each():
			# main_dict[farmer_key] = {}
			# print(farmer_key.key())
			# print(farmer_key.val())
			
			main_list = []
			description = {}
			for broadcast_key,value in farmer_key.val().items():
				broadcast = {}
				coordinates = []
				# print("HIIJIHEIGHE")
				# print(value)
				# print(value['latitude'])
				coordinates.append(value['latitude'])
				coordinates.append(value['longitude'])
				broadcast['coordinates'] = coordinates
				print(coordinates)
				broadcast['availableQuantity'] = value['availableQuantity']
				broadcast['cropName'] = value['cropName']
				broadcast['expectedPrice'] = value['expectedPrice']
				# print(broadcast)
				description[broadcast_key] = broadcast
				# print('-------------------')
				main_list.append(description)
			# print(main_list)
			main_dict[farmer_key.key()] = main_list
		# print('gjsygfjwgfwgfyku')
		# print(main_dict)
		count = 0
		for key,val in main_dict.items():
			for v in val:
				count = count + 1
		print(count)
		# print(main_dict)
		data = {'f1' : {'b1':{'cropName' : 'ketchup','expectedPrice':200,'availableQuantity' : 500, 'coordinates':[-96, 37.8]}},'f2':{'b2':{'cropName' : 'wheat','expectedPrice':800,'availableQuantity' : 900, 'coordinates':[-90, 40]}}}
		# mapbox_access_token = 'pk.eyJ1IjoiZGVlcGlrYXBvbWVuZGthciIsImEiOiJjazFsMWd4d3QwMHdpM21uc3U3OGxrbndlIn0.6Cj2VYFMQq8V6TCYLIySzg'
		return JsonResponse(main_dict,safe = False)

def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoiZGVlcGlrYXBvbWVuZGthciIsImEiOiJjazFsMWd4d3QwMHdpM21uc3U3OGxrbndlIn0.6Cj2VYFMQq8V6TCYLIySzg'
    return render(request,'marker/marker_default.html',{ 'mapbox_access_token': mapbox_access_token })
