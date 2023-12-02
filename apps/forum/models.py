from django.contrib.auth.models import User
from django.db import models

class subject (models.Model):
    text =








class Question(models.Model):
    text = models.CharField(max_length=255)
    userid = models.ForeignKey(User, on_delete=models.PROTECT)
    stasus = models.BooleanField(default=False)
    created_at = models.DateField()
    #topic_id = models.ForeignKey(topic, on_delete=models.CASCADE)//


class Answers(models.Model):
    text = models.CharField()
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.BooleanField(default=False)
    created_at = models.DateField()
    question_id = models.ForeignKey(Question,on_delete=models.CASCADE)









