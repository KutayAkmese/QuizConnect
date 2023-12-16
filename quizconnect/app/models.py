from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=50)
    user_image = models.ImageField(upload_to ='uploads/user')

class Lessons(models.Model):
    name = models.CharField(max_length=200)
    lesson_code = models.CharField(max_length=10)
    lecturer = models.CharField(max_length=200)

class Questions(models.Model):
    question_text = models.TextField()
    question_image = models.ImageField(upload_to ='uploads/questions')
    star_number = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)

class Answers(models.Model):
    answer_image = models.ImageField(upload_to ='uploads/answers')
    star_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)

class TimeLineItems(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
   