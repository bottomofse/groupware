from django.db import models
from accounts.models import Employee
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=150)
    contents = models.CharField(max_length=800)
    pub_date = models.DateTimeField(default=timezone.now())

    contributer = models.CharField(max_length=150)

    def __str__(self):
        return self.title
