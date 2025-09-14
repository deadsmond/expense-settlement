from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import GroupViewSet, ExpenseViewSet, UserViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"groups", GroupViewSet, basename="group")
router.register(r"expenses", ExpenseViewSet, basename="expense")

urlpatterns = [path("", include(router.urls)), path("auth/", obtain_auth_token)]
