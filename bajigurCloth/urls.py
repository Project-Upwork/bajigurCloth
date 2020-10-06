from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
    path('accounts/login/', admin.site.urls),
    path('api/v1/wish/', include('api._wish.urls')),
    path('api/v1/crm/', include('api._crm.urls')),
]
