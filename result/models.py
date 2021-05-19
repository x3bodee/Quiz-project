from django.db import models
from quiz.models import Quiz
from user.models import User
from datetime import datetime


# Create your models here.

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    date = models.DateField(null=True , default=datetime.now)

    def __str__(self):
        return str(self.pk)+ "-" + str(self.score)
