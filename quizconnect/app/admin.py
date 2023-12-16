from django.contrib import admin

# Register your models here.
from .models import User, Lesson, Question, Answer, TimeLineItem

admin.site.register(User)
admin.site.register(Lesson)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(TimeLineItem)

