from django.shortcuts import render
from .models import User


# Login page
def login(request):
    return render(request, "login.html")

# Register page
def register(request):
    return render(request, "register.html")

def addUser(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
    return render(request, "login.html")

def loginUser(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    try:
        if User.objects.filter(email=email).filter(password=password):
            return render(request, "index.html")
        else:
            return render(request, "login.html")
    except:
        print("Failed to query from models")
        return render(request, "login.html")

# Home page / Time line
def home(request): 
     
    return render(request,"index.html")

# Lessons pages
def lessons(request):
    return render(request,"lessons.html")

# Lessons detial
def lessonDetails(request):
    return render(request,"details.html")



# Profile page
def profile(request):
    return render(request, "profile.html")

def addQuestion(request):
    return render(request, "addQuestion.html")

def questionDetail(request):
    return render(request, "details.html")