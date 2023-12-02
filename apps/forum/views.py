from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.forum.models import Question


@login_required
def index(request):
    question_list = Question.objects.filter(is_active=True)
    context = {'question_list': question_list}
    return render(request, "index.html", context)


def question_add(request):
    context = {

    }
    return render(request, "apps/forum/question_add.html", context)
