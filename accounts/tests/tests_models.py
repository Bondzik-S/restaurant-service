from django.test import TestCase
from django.contrib.auth import get_user_model

from restaurant.forms import CookCreationForm


Cook = get_user_model()

class CookModelTest(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create_user(
            username='testcook', password='password123', years_of_experience=5
        )

    def test_cook_creation(self):
        self.assertEqual(self.cook.username, 'testcook')
        self.assertTrue(self.cook.check_password('password123'))

    def test_years_of_experience_validation(self):
        data = {
            'username': 'invalid',
            'password1': 'password123',
            'password2': 'password123',
            'years_of_experience': 0,
            'first_name': 'Test',
            'last_name': 'User',
        }
        form = CookCreationForm(data)

        self.assertFalse(form.is_valid())

        self.assertIn('years_of_experience', form.errors)
        self.assertEqual(
            form.errors['years_of_experience'][0],
            'Years of experience cannot be less than 1'
        )
