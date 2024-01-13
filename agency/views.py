from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from agency.models import Redactor, Topic, Newspaper

@login_required
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


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "agency/redactor_list.html"
    context_object_name = "redactor_list"
    paginate_by = 3


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    template_name = "agency/newspaper_list.html"
    context_object_name = "newspaper_list"
    paginate_by = 4


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = "agency/topic_list.html"
    context_object_name = "topic_list"
    paginate_by = 5


class TopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Topic

