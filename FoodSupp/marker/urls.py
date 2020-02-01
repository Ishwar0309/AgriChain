from . import views
from django.urls import path

urlpatterns = [
	path('',views.default_map,name='default_map'),
	path('map/',views.map_analyse,name='map_analyse'),
]