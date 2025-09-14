import pytest
from django.contrib.auth import get_user_model
from core.models import Group, Expense

User = get_user_model()

@pytest.mark.django_db
def test_create_group_and_expense():
    user = User.objects.create_user(username="alice", password="pass123")
    group = Group.objects.create(name="Trip")
    group.members.add(user)

    expense = Expense.objects.create(
        group=group,
        paid_by=user,
        amount=100.00,
        description="Hotel"
    )

    assert expense.amount == 100.00
    assert expense.paid_by == user
    assert expense.group == group
