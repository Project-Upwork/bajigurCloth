from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views

schema_view = get_swagger_view(title="Creator Wish")

urlpatterns =[
    path('docs/', schema_view),
    path('account/',include('api._wish.account.urls')),
    path('creator/',include('api._wish.creator.urls')),
    path('auth-token/', views.obtain_auth_token)
]