from django.db import models

# Create your models here.
DIFF_CHOICES =(
    ('easy','easy'),
    ('medium','medium'),
    ('hard','hard'),
)

class Quiz (models.Model):
    name =models.CharField(max_length=150)
    number_of =models.IntegerField()
    time=models.IntegerField()
    score_to_pass=models.IntegerField()
    difficulty=models.CharField(max_length=15,choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}-{self.difficulty}"

    def get_questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name_plural = 'Quizes'
