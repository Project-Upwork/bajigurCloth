from django.urls import path, include
from .views import TaskList

urlpatterns =[
    path("", TaskList.as_view(), name='task')
]