import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField("Texto da questão", max_length=200)
    pub_date = models.DateTimeField("Data da publicação", default=timezone.now)
    active = models.BooleanField("Ativo", default=True)

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        verbose_name = "Questão"
        verbose_name_plural = "Questões"


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="Questão"
    )
    choice_text = models.CharField("Descrição", max_length=200)
    vote = models.IntegerField("Votos", default=0)

    def __str__(self) -> str:
        return f"{self.question.id} e {self.choice_text}"

    class Meta:
        verbose_name = "Opção"
        verbose_name_plural = "Opções"
