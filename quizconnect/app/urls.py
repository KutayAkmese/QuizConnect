from django.urls import path
from . import views

urlpatterns=[
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("add", views.addQuestion, name="addQuestion"),
    path("details", views.questionDetail, name="details"),
    path("leesons", views.lessons, name="lessons"),
    path("lessons/<str:name>", views.lessonDetails, name="lessonDetails"),
]