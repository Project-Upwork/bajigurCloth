from django.urls import path, include
from .views import DelegationList

urlpatterns =[
    path("", DelegationList.as_view(), name='task')
]