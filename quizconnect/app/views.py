from django.shortcuts import render



# Home page / Time line
def home(request):
    return render(request,"index.html")

# Lessons pages
def lessons(request):
    return render(request,"lessons.html")

# Lessons detial
def lessonDetails(request):
    return render(request,"details.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")