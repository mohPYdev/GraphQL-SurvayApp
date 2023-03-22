from django.db import models
# Create your models here.


class User(models.Model):
    ''' django model for users '''
    pass


class Form(models.Model):
    ''' django model for forms '''
    
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_created=True)
    number_participants = models.IntegerField(null=True, blank=True)


class Question(models.Model):
    ''' django model for questions '''

    form  = models.ForeignKey(Form, on_delete=models.CASCADE)
    correct_ans_rate = models.FloatField(null=True, blank=True)
    text = models.CharField(max_length=200)


class Answer(models.Model):
    ''' django model for answers '''

    question  = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans_rate = models.FloatField(null=True, blank=True)
    text = models.CharField(max_length=200)
    

class Response(models.Model):
    ''' django model for user responses '''

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    date_issued = models.DateTimeField(auto_now=True)
