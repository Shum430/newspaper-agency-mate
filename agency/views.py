from django.shortcuts import render
from agency.models import Redactor, Topic, Newspaper


def index(request):
    redactors = Redactor.objects.all()
    topics = Topic.objects.all()
    newspapers = Newspaper.objects.all()
    context = {
        "redactors": redactors,
        "newspapers": newspapers,
        "topics": topics
    }
    return render(request, "agency/index.html", context=context)
