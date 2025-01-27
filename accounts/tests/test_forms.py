from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.forms import CookCreationForm, CookUpdateForm


Cook = get_user_model()


class TestCookCreationForm(TestCase):
    def test_valid_data(self):
        form = CookCreationForm(data={
            "username": "cook1",
            "password1": "validpassword123",
            "password2": "validpassword123",
            "years_of_experience": 5,
            "first_name": "John",
            "last_name": "Doe",
        })
        self.assertTrue(form.is_valid())

    def test_invalid_years_of_experience_negative(self):
        form = CookCreationForm(data={
            "username": "cook1",
            "password1": "validpassword123",
            "password2": "validpassword123",
            "years_of_experience": -1,
            "first_name": "John",
            "last_name": "Doe",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("Years of experience cannot be less than 1", form.errors["years_of_experience"])

    def test_invalid_years_of_experience_too_high(self):
        form = CookCreationForm(data={
            "username": "cook1",
            "password1": "validpassword123",
            "password2": "validpassword123",
            "years_of_experience": 60,
            "first_name": "John",
            "last_name": "Doe",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("Years of experience cannot be more than 55", form.errors["years_of_experience"])


class TestCookUpdateForm(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create_user(
            username="cook1",
            password="validpassword123",
            years_of_experience=5,
            first_name="John",
            last_name="Doe",
        )

    def test_valid_update(self):
        form = CookUpdateForm(data={
            "username": "cook1",
            "years_of_experience": 10,
            "first_name": "John",
            "last_name": "Smith",
        }, instance=self.cook)
        self.assertTrue(form.is_valid())

    def test_invalid_update(self):
        form = CookUpdateForm(data={
            "username": "cook1",
            "years_of_experience": -2,
            "first_name": "John",
            "last_name": "Smith",
        }, instance=self.cook)
        self.assertFalse(form.is_valid())
        self.assertIn("Years of experience cannot be less than 1", form.errors["years_of_experience"])
