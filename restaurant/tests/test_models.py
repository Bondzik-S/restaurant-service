from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import Dish, DishType
from accounts.models import Cook


class ModelTests(TestCase):
    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="Test Dish Type"
        )
        dish = Dish.objects.create(
            name="test",
            dish_type=dish_type,
            price=5.66
        )
        self.assertEqual(
            str(dish), f"{dish.name}"
        )

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="nina.vas",
            first_name="Nina",
            last_name="Vasylenko"
        )
        self.assertEqual(
            str(cook),
            f"{cook.username}"
        )

    def test_create_cook_with_years_of_experience(self):
        username = "pipi"
        years_of_experience = 4
        password = "546tttt454"
        cook = get_user_model().objects.create_user(
            username=username,
            years_of_experience=years_of_experience,
            password=password
        )
        self.assertEqual(cook.username, username)
        self.assertEqual(cook.years_of_experience, years_of_experience)
        self.assertTrue(cook.check_password(password))

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="Test dish took"
        )
        self.assertEqual(
            str(dish_type),
            f"{dish_type.name}"
        )