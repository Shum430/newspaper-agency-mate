from django.contrib.auth import get_user_model
from django.test import TestCase

from agency.models import Topic, Newspaper


class ModelTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(name="Test Topic")
        self.assertEqual(str(topic), topic.name)

    def test_newspaper_str(self):
        topic = Topic.objects.create(name="test")
        newspaper = Newspaper.objects.create(
            title="Test",
            content="test content",
            published_date="2022-01-01",
            topic=topic
        )
        self.assertEqual(str(newspaper), newspaper.title)

    def test_create_redactor_with_years_of_experience(self):
        username = "test"
        password = "test123"
        years_of_experience = 2
        redactor = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )
        self.assertEqual(redactor.username, username)
        self.assertEqual(redactor.years_of_experience, years_of_experience)
        self.assertTrue(redactor.check_password(password))
