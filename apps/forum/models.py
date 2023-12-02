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







class answers (models.Model):









