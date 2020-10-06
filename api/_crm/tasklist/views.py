from rest_framework import generics, permissions
from api._wish.permissions import IsAdminOrReadOnly, MemberAccessPermission
from simplycrm.models import JobDesk
from .serializers import JobDeskSerializer

class TaskList(generics.ListAPIView):
    queryset = JobDesk.objects.all()
    serializer_class = JobDeskSerializer
    permission_classes = (MemberAccessPermission,)
