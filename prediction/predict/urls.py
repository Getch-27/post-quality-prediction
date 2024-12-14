from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_price, name='predict_price'),
    path('reputation/', views.predict_rep, name= "predict_rep")
]