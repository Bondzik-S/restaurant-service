from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self) -> str:
        return self.username

    def get_absolute_url(self) -> str:
        return reverse("restaurant:cooks-detail", kwargs={"pk": self.pk})
