from django.urls import path
from . import views

urlpatterns=[
    path("", views.home,name="home"),
    path("home", views.home),
    path("unterrichten",views.unterricht,name="unterrichten"),
    path("unterrichten/<str:name>",views.unterrichtendetails,name="dersdetails"),
]