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

# Login page
def login(request):
    return render(request, "login.html")

# Register page
def register(request):
    return render(request, "register.html")

# Profile page
def profile(request):
    return render(request, "profile.html")

def addQuestion(request):
    return render(request, "addQuestion.html")

def questionDetail(request):
    return render(request, "details.html")