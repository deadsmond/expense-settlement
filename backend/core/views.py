from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Group, Expense, User
from .serializers import GroupSerializer, ExpenseSerializer, UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Group.objects.filter(members=self.request.user)

    def perform_create(self, serializer):
        group = serializer.save()
        group.members.add(self.request.user)

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def add_member(self, request, pk=None):
        group = self.get_object()
        user_id = request.data.get("user_id")
        user = User.objects.get(pk=user_id)
        group.members.add(user)
        return Response({"status": "user added"})

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(group__members=self.request.user)

    def perform_create(self, serializer):
        serializer.save(paid_by=self.request.user)

    @action(detail=False, methods=["get"], permission_classes=[permissions.IsAuthenticated])
    def summary(self, request):
        user = request.user
        groups = Group.objects.filter(members=user)
        data = {}

        for group in groups:
            expenses = Expense.objects.filter(group=group)
            members = list(group.members.all())
            member_count = len(members)
            balances = {member.id: 0 for member in members}

            for expense in expenses:
                share = float(expense.amount) / member_count
                for member in members:
                    if member == expense.paid_by:
                        balances[member.id] += float(expense.amount) - share
                    else:
                        balances[member.id] -= share

            data[group.id] = {
                "group_name": group.name,
                "balances": {User.objects.get(id=k).username: round(v, 2) for k, v in balances.items()}
            }

        return Response(data)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
