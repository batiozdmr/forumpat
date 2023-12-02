from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=120, blank=False)
    created_at = models.DateField()
    is_active = models.BooleanField(default=False)
