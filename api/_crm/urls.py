from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views

schema_view = get_swagger_view(title="Simply CRM")

urlpatterns =[
    path('docs/', schema_view),
    path('task/', include('api._crm.tasklist.urls')),
    path('delegation/', include('api._crm.delegation.urls'))
]