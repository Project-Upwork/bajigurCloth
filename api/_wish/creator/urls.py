from django.urls import path, include
from .views import WishList, WishCreate

urlpatterns = [
   path("", WishList.as_view(), name="list-wish"),
   path("create/", WishCreate.as_view(), name="create-wish")
]