from django.db import models
from quiz.models import Quiz

# Create your models here.

TYPE_CHOICES =(
    ('multiple','multiple'),
    ('True or False','True or False'),
)

class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    type=models.CharField(max_length=255,choices=TYPE_CHOICES)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"