from django.urls import path

from agency.views import index, RedactorListView, RedactorDetailView

urlpatterns = [
    path("", index, name="index"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail")
]

app_name = "agency"
