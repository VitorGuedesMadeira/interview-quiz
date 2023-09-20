from django.db import models

# Create your models here.

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

class Option(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  option_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  correct = models.BooleanField()

