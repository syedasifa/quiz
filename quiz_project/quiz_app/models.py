from django.db import models
from django.contrib.auth.models import User

# class Quizz(models.Model):

# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	question = models.Many



class Question(models.Model):

	question = models.CharField(max_length=252)
	user = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return f'{self.question}'


class Options(models.Model):

	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	option = models.CharField(max_length=252)

	def __str__(self):
		return f"{self.option}"