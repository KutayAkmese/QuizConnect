from django.shortcuts import render, redirect
from .models import User, Question, TimeLineItem
from django.http import Http404

# Home page / Time line
def home(request, user_id): 
    mainUser = User.objects.get(id=user_id)
    timeLineItems = TimeLineItem.objects.all().order_by("-id")
    return render(request,"index.html", {
        'user': mainUser,
        'timeLineItems': timeLineItems,
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
                return redirect('home/' + str(user.id))
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
            return redirect('home/' + str(user.id))
        except:
            # Burada bir hata mesaji gonderilecek. 
            return redirect('register')
    else:
        return render(request, "register.html")
    
def addQuestion(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST": 
        questionText = request.POST.get("questionText")
        imageFile = request.POST.get("imageFile")
        questionTitle = request.POST.get("questionTitle")
        lessonSelection = request.POST.get("lessonSelection")
        question = Question(question_title=questionTitle, question_image=imageFile, 
                            question_text=questionText, user_id= user.id, lesson_id=1)
        question.save()
        timeLineItem = TimeLineItem(question_id=question.id, user_id=user.id)
        timeLineItem.save()
        return redirect('http://127.0.0.1:8000/home/' + str(user.id))

    return render(request, "addQuestion.html", {
        'user': user
    })
   
# Profile page
def profile(request, user_id):
    user = User.objects.get(id=user_id)

    return render(request, "profile.html", {
        'user':user
    }) 
    
# Lessons pages
def lessons(request, user_id):
    user = User.objects.get(id=user_id)
    
    return render(request,"lessons.html", {
        'user': user
    })

# Lessons detial
def lessonDetails(request, user_id):
    user = User.objects.get(id=user_id)

    return render(request,"details.html", {
        'user': user
    })


def questionDetail(request, user_id, item_id):
    user = User.objects.get(id=user_id)
    timeLineItem = TimeLineItem.objects.get(id=item_id)
    

    return render(request,"details.html", {
        'user': user,
        'timeLineItem': timeLineItem,
    })
    
def like(request, user_id, item_id):
    user = User.objects.get(pk=user_id)
    question_id = TimeLineItem.objects.filter(id=item_id).values_list('question_id', flat=True)
    question = Question.objects.get(id=question_id[0])
    question.star_number = question.star_number + 1
    question.save()
  
    return redirect('http://127.0.0.1:8000/home/'+ str(user.id))
    

