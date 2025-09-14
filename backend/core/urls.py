from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, ExpenseViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r"groups", GroupViewSet)
router.register(r"expenses", ExpenseViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
