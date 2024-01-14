from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from agency.forms import RedactorCreationForm, NewspaperForm
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


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    fields = ("username", "first_name", "last_name", "years_of_experience",)
    success_url = reverse_lazy("agency:redactor-list")
    template_name = "agency/redactor_form.html"


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-list")
    template_name = "agency/redactor_confirm_delete.html"


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    template_name = "agency/newspaper_list.html"
    context_object_name = "newspaper_list"
    paginate_by = 4


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    template_name = "agency/newspaper_confirm_delete.html"


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = "agency/topic_list.html"
    context_object_name = "topic_list"
    paginate_by = 5


class TopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Topic


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")
    template_name = "agency/topic_form.html"


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")
    template_name = "agency/topic_form.html"


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    template_name = "agency/topic_confirm_delete.html"


