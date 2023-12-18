from django.shortcuts import render, redirect
from .models import User

# Home page / Time line
def home(request, user_id): 
    user = User.objects.get(id=user_id)
    print(user.first_name)
    return render(request,"index.html", {
        'user': user,
        'userName': user.first_name 
        })

# Login page
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:    
            user = User.objects.filter(email=email).filter(password=password)
            if user:
                id = User.objects.get(email=email).id
                return redirect('home/' + str(id))
            else:
                return redirect('login')
        except:
            print("Failed to query from models")
            return render(request, "login.html")
    else:
        return render(request, "login.html")

# Register page
def register(request):
    if request.method == "POST":
        try: 
            first_name = request.POST.get("firstName")
            last_name = request.POST.get("lastName")
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = User(first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            return redirect('home')
        except:
            # Burada bir hata mesaji gonderilecek. 
            return redirect('register')
    else:
        return render(request, "register.html")
    

# Lessons pages
def lessons(request):
    return render(request,"lessons.html")

# Lessons detial
def lessonDetails(request):
    return render(request,"details.html")

# Profile page
def profile(request, user_id):
    user = User.objects.get(id=user_id)

    return render(request, "profile.html", {
        'user':user
    })

def addQuestion(request):
    return render(request, "addQuestion.html")

def questionDetail(request):
    return render(request, "details.html")