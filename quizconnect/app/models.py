from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=50)
    user_image = models.ImageField(upload_to ='uploads/user', null=True)
    
    def __str__(self): 
        return self.first_name + " " + self.last_name
    
class Lesson(models.Model):
    name = models.CharField(max_length=200)
    lesson_code = models.CharField(max_length=10, null=False, unique=True)
    lecturer = models.CharField(max_length=200)
        
    def __str__(self): 
        return self.name
    
class Question(models.Model):
    question_title = models.TextField(default="An explanation is needed for the question here.")
    question_text = models.TextField(default="An explanation is needed for the question here.")
    question_image = models.ImageField(upload_to ='media/')
    star_number = models.IntegerField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    def __str__(self): 
        return self.question_text[0:100]

class TimeLineItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self): 
        return self.user.first_name + self.user.last_name + '||' + self.question.question_text[0:100]

class Answer(models.Model):
    answer_text = models.TextField(default="An explanation is needed for the answer here.")
    answer_image = models.ImageField(upload_to ='uploads/answers', blank=True)
    star_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self): 
        return self.answer_text[0:100]
    


   