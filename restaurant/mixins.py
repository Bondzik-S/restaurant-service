class SearchFormMixin:
    search_form_class = None
    search_field_name = None

    def get_search_query(self):
        return self.request.GET.get(self.search_field_name, "")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.get_search_query()
        context["search_form"] = self.search_form_class(initial={self.search_field_name: search_query})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.get_search_query()
        if self.search_form_class:
            form = self.search_form_class(self.request.GET)
            if form.is_valid():
                filter_kwargs = {f"{self.search_field_name}__icontains": form.cleaned_data[self.search_field_name]}
                return queryset.filter(**filter_kwargs)
        return queryset
