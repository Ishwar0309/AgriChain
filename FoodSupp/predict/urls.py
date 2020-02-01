
from django.urls import path,include
from predict import views

urlpatterns = [
    path('',views.home,name='home'),
    path('analyzeArea/',views.analyse,name='analyseArea'),
    path('analyzeArea/predict',views.predict,name='predict'),
]