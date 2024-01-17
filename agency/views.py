from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from agency.forms import RedactorCreationForm, NewspaperForm, RedactorSearchForm, NewspaperSearchForm
from agency.models import Redactor, Topic, Newspaper


class IndexView(ListView):
    template_name = "agency/index.html"
    context_object_name = "context"
    queryset = Newspaper.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["redactors"] = Redactor.objects.all()
        return context


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "agency/redactor_list.html"
    context_object_name = "redactor_list"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorListView, self).get_context_data(**kwargs)
        context["search_form"] = RedactorSearchForm()
        return context

    def get_queryset(self):
        username = self.request.GET.get("username")
        if username:
            return Redactor.objects.filter(username__icontains=username)
        return Redactor.objects.all()


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        redactor = self.object
        topics_count = {}
        for newspaper in redactor.redactors_newspapers.all():
            topic_name = newspaper.topic.name
            topics_count[topic_name] = topics_count.get(topic_name, 0) + 1

        if topics_count:
            most_popular_topic = max(topics_count, key=topics_count.get)
        else:
            most_popular_topic = "No assigned newspapers"

        context['most_popular_topic'] = most_popular_topic

        return context


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm

    def get_success_url(self):
        return reverse_lazy("agency:redactor-list")


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)
        context["search_form"] = NewspaperSearchForm()
        return context

    def get_queryset(self):
        start_date = self.request.GET.get("start_date")
        end_date = self.request.GET.get("end_date")
        if start_date and end_date:
            return Newspaper.objects.filter(published_date__range=(start_date, end_date))
        return Newspaper.objects.all()


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = "agency/newspaper_form.html"
    success_url = reverse_lazy("agency:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("agency:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    template_name = "agency/newspaper_confirm_delete.html"
    success_url = reverse_lazy("agency:newspaper-list")


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = "agency/topic_list.html"
    context_object_name = "topic_list"
    paginate_by = 2


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
    success_url = reverse_lazy("agency:topic-list")





