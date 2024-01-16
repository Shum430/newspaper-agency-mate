from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from agency.forms import RedactorCreationForm


class FormsTest(TestCase):
    def test_redactor_creation_form_with_years_of_experience_valid(self):
        form_data = {
            "username": "test_user",
            "password1": "test_password",
            "password2": "test_password",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "years_of_experience": 2
        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class PrivateRedactorTesta(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test_password"
        )
        self.client.force_login(self.user)

    def test_redactor_created(self):
        form_data = {
            "username": "test_user",
            "password1": "test_password",
            "password2": "test_password",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "years_of_experience": 2
        }
        self.client.post(reverse("agency:redactor-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])
        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.years_of_experience, form_data["years_of_experience"])
