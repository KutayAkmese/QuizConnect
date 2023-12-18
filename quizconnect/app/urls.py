from django.urls import path
from . import views
from .models import User


urlpatterns=[
    path("", views.login, name="login"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("home/<str:user_id>", views.home, name="home"),
    path("profile<str:user_id>", views.profile, name="profile"),
    path("add", views.addQuestion, name="addQuestion"),
    path("details", views.questionDetail, name="details"),
    path("leesons", views.lessons, name="lessons"),
    path("lessons/<str:name>", views.lessonDetails, name="lessonDetails"),
]