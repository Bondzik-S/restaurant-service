from django.test import TestCase

from restaurant.forms import CookCreationForm


class FormsTests(TestCase):
    def test_chef_creation_form_is_valid(self):
        form_data = {
            "username": "mimi_lis",
            "password1": "mmmimi453a",
            "password2": "mmmimi453a",
            "first_name": "Mimi",
            "last_name": "Lis",
            "years_of_experience": 7
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)