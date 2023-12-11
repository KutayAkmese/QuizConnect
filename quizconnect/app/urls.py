from django.urls import path
from . import views

urlpatterns=[
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("leesons", views.lessons, name="lessons"),
    path("lessons/<str:name>", views.lessonDetails, name="lessonDetails"),
]