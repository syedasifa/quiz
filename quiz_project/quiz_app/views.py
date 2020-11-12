from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Question, Options


@login_required
def dashboard(request):
	""" Used to land into this page after login"""

	query = Options.objects.all()

	questions_dict = {}
	for value in query:
		question = value.question.question
		options = [option.option for option in query]
		questions_dict.update({question: options})

	return render(request, 'quiz_app/dashboard.html', {'questions': questions_dict, 'options': options})

