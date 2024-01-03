from django.urls import path
from . import views
from .models import User
from django.conf import settings

from django.conf.urls.static import static



urlpatterns=[
    path("", views.login, name="login"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("home/<str:user_id>", views.home, name="home"),
    path("profile/<str:user_id>", views.profile, name="profile"),
    path("add/<str:user_id>", views.addQuestion, name="addQuestion"),
    path("details/<str:user_id>/<str:item_id>", views.questionDetail, name="details"),
    path("lessons/<str:user_id>", views.lessons, name="lessons"),
    path("like/<str:user_id>/<str:item_id>", views.like, name="like"),
    path("search/<str:user_id>", views.search, name="search"),
    path("addLesson/<str:user_id>", views.addLesson, name="addLesson"),
    path("go_questions/<str:user_id>/<str:lesson_id>", views.go_questions, name="go_questions"),
    path("addAnswer/<str:user_id>/<str:item_id>", views.addAnswer, name="addAnswer"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)