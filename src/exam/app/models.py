from django.db import models
from django.contrib.auth.models import User

class Exam(models.Model):
    title = models.CharField(max_length=100)
    times_taken = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Question(models.Model):
    exam = models.ForeignKey(Exam)
    text = models.CharField(max_length=200)
    correct_answer = models.IntegerField(default=0) #models.ForeignKey(Option, blank=True, null=True)

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.text
    
