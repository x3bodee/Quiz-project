from django.db import models
import random 
from user.models import User
from datetime import datetime
# Create your models here.
DIFF_CHOICES =(
    ('easy','easy'),
    ('medium','medium'),
    ('hard','hard'),
)

class Quiz (models.Model):
    name =models.CharField(max_length=150)
    number_of_question =models.IntegerField()
    time=models.IntegerField()
    score_to_pass=models.IntegerField()
    difficulty=models.CharField(max_length=15,choices=DIFF_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_type= models.BooleanField(default=True)
    date = models.DateField(null=True , default=datetime.now)

    

    def __str__(self):
        return f"{self.name}"

    def get_questions(self):
        questions= list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_question]

    class Meta:
        verbose_name_plural = 'Quizes'
