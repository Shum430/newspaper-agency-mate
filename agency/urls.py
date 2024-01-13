from django.urls import path

from agency.views import (
    index,
    RedactorListView,
    RedactorDetailView,
    NewspaperListView,
    NewspaperDetailView,
    TopicListView,
    TopicDetailView, RedactorCreateView, NewspaperCreateView, TopicCreateView
)

urlpatterns = [
    path("", index, name="index"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
    path("redactors/create/", RedactorCreateView.as_view(), name="redactor-create"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("newspapers/create/", NewspaperCreateView.as_view(), name="newspaper-create"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/<int:pk>/", TopicDetailView.as_view(), name="topic-detail"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
]

app_name = "agency"
