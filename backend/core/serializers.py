from rest_framework import serializers
from .models import Group, Expense, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class GroupSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    member_ids = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, write_only=True, source="members"
    )

    class Meta:
        model = Group
        fields = ["id", "name", "members", "member_ids"]

class ExpenseSerializer(serializers.ModelSerializer):
    paid_by = UserSerializer(read_only=True)

    class Meta:
        model = Expense
        fields = ["id", "group", "paid_by", "amount", "description", "created_at"]

    def create(self, validated_data):
        validated_data["paid_by"] = self.context["request"].user
        return super().create(validated_data)
