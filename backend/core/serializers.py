from rest_framework import serializers
from .models import Group, Expense

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"
