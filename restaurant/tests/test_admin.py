from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import Cook
from restaurant.models import DishType, Dish


class AdminSiteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin1234"
        )
        self.client.force_login(self.admin_user)

        # Створюємо Cook
        self.cook = Cook.objects.create_user(
            username="cook1",
            password="cook1234",
            years_of_experience=10
        )

        self.dish_type = DishType.objects.create(name="Main Course")

        self.dish = Dish.objects.create(
            name="Dish 1",
            price=100.0,
            dish_type=self.dish_type
        )
        self.dish.cooks.add(self.cook)

    def test_dish_type_list_display(self):
        url = reverse("admin:restaurant_dishtype_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.dish_type.name)

    def test_dish_type_search(self):
        url = reverse("admin:restaurant_dishtype_changelist")
        res = self.client.get(url + "?q=Main")
        self.assertContains(res, self.dish_type.name)

    def test_dish_list_display(self):
        url = reverse("admin:restaurant_dish_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.dish.name)
        self.assertContains(res, self.dish.price)
        self.assertContains(res, self.dish.dish_type.name)

    def test_dish_list_filter_by_dish_type(self):
        url = reverse("admin:restaurant_dish_changelist")
        res = self.client.get(url + "?dish_type__id=" + str(self.dish.dish_type.id))
        self.assertContains(res, self.dish.name)

    def test_dish_search_by_name(self):
        url = reverse("admin:restaurant_dish_changelist")
        res = self.client.get(url + "?q=Dish 1")
        self.assertContains(res, self.dish.name)

    def test_dish_search_by_dish_type(self):
        url = reverse("admin:restaurant_dish_changelist")
        res = self.client.get(url + "?q=Main Course")
        self.assertContains(res, self.dish.name)
