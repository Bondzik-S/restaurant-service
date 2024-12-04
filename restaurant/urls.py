"""
URL configuration for restaurant_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from restaurant.views import index, CookersListView, CookersCreateView, CookersUpdateView, CookerDetailView, \
    CookersDeleteView, DishListView, DishDetailView, DishCreateView, DishUpdateView, DishDeleteView, \
    assign_cook_to_dish, DishTypeListView, DishTypeCreateView, DishTypeUpdateView, \
    DishTypeDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("cookers/", CookersListView.as_view(), name="cookers-list"),
    path("cookers/<int:pk>/", CookerDetailView.as_view(), name="cookers-detail"),
    path("cookers/create/", CookersCreateView.as_view(), name="cookers-create"),
    path("cookers/<int:pk>/update/", CookersUpdateView.as_view(), name="cookers-update"),
    path("cookers/<int:pk>/delete/", CookersDeleteView.as_view(), name="cookers-delete"),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path(
        "dish/<int:pk>/toggle-assign/",
        assign_cook_to_dish,
        name="toggle-car-assign",
    ),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("dish-type/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-type/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish-type/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish-type/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
]

app_name = "restaurant"
