from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from agency.models import Redactor, Newspaper, Topic


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + ("years_of_experience", "first_name", "last_name")


class NewspaperForm(forms.ModelForm):
    redactors = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    topic = forms.ModelChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.Select,
        required=True
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        )
    )

