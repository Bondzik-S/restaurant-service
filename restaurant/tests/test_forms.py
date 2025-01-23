from django.test import TestCase
from django.contrib.auth import get_user_model

from restaurant.forms import (
    DishForm,
    CookSearchForm,
    DishSearchForm,
    DishTypeSearchForm,
)
from restaurant.models import DishType


User = get_user_model()


class TestDishForm(TestCase):
    def setUp(self):
        self.cook1 = User.objects.create_user(username="cook1", password="password123")
        self.cook2 = User.objects.create_user(username="cook2", password="password123")
        self.dish_type = DishType.objects.create(name="Main Course")

    def test_valid_dish(self):
        form = DishForm(data={
            "name": "Dish1",
            "description": "Delicious dish",
            "price": 12.99,
            "dish_type": self.dish_type.id,
            "cooks": [self.cook1.id, self.cook2.id],
        })
        self.assertTrue(form.is_valid())

    def test_missing_name(self):
        form = DishForm(data={
            "description": "Delicious dish",
            "price": 12.99,
            "dish_type": self.dish_type.id,
            "cooks": [self.cook1.id, self.cook2.id],
        })
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)


class TestSearchForms(TestCase):
    def test_cook_search_form(self):
        form = CookSearchForm(data={"username": "testcook"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "testcook")

    def test_dish_search_form(self):
        form = DishSearchForm(data={"name": "Pizza"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "Pizza")

    def test_dish_type_search_form(self):
        form = DishTypeSearchForm(data={"name": "Main Course"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "Main Course")
