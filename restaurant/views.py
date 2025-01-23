from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from accounts.models import Cook
from restaurant.forms import (
    CookSearchForm,
    DishSearchForm,
    DishForm,
    CookCreationForm,
    CookUpdateForm,
    DishTypeSearchForm
)
from restaurant.mixins import SearchFormMixin
from restaurant.models import DishType, Dish


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = "restaurant/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            "num_cooks": Cook.objects.count(),
            "num_dishes_types": DishType.objects.count(),
            "num_dishes": Dish.objects.count(),
            "num_visits": self.request.session.get("num_visits", 0) + 1,
        })

        self.request.session["num_visits"] = context["num_visits"]

        return context


class CooksListView(LoginRequiredMixin, SearchFormMixin, generic.ListView):
    model = Cook
    template_name = "restaurant/cooks_list.html"
    paginate_by = 5
    search_form_class = CookSearchForm
    search_field_name = "username"


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes__dish_type")
    template_name = "restaurant/cook_detail.html"


class CooksCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("restaurant:cooks-list")
    template_name = "restaurant/cook_form.html"


class CooksUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm
    success_url = reverse_lazy("restaurant:cooks-list")
    template_name = "restaurant/cook_form.html"


class CooksDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("restaurant:cooks-list")
    template_name = "restaurant/cook_confirm_delete.html"


class DishListView(LoginRequiredMixin, SearchFormMixin, generic.ListView):
    model = Dish
    template_name = "restaurant/dishes_list.html"
    paginate_by = 5
    search_form_class = DishSearchForm
    search_field_name = "name"


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("restaurant:dishes-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("restaurant:dishes-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("restaurant:dishes-list")


class DishTypeListView(LoginRequiredMixin, SearchFormMixin, generic.ListView):
    model = DishType
    template_name = "restaurant/dish_type_list.html"
    paginate_by = 5
    search_form_class = DishTypeSearchForm
    search_field_name = "name"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = ["name", ]
    success_url = reverse_lazy("restaurant:dish-types-list")
    template_name = "restaurant/dish_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = ["name",]
    template_name = "restaurant/dish_form.html"
    success_url = reverse_lazy("restaurant:dish-types-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("restaurant:dish-types-list")
    template_name = "restaurant/dish_type_confirm_delete.html"


@login_required
def assign_cook_to_dish(request, pk):
    dish = get_object_or_404(Dish, id=pk)

    if not dish.cooks.filter(id=request.user.id).exists():
        dish.cooks.add(request.user)
    else:
        dish.cooks.remove(request.user)

    return redirect("restaurant:dish-detail", pk=pk)
