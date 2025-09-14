from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Group(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name="groups")


class Expense(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
