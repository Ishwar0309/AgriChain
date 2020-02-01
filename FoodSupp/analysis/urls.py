from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='new_index'),
    path('data/',views.analyse,name='analyse'),
]
