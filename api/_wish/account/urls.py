from django.urls import path, include
from .views import AccountList

urlpatterns = [
   path("", AccountList.as_view(), name="account-list"),
]