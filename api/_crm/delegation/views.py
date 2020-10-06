from rest_framework import generics, permissions
from api._wish.permissions import IsAdminOrReadOnly, MemberAccessPermission
from simplycrm.models import Staff
from .serializers import DelegationSerializer

class DelegationList(generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = DelegationSerializer
    permission_classes = (MemberAccessPermission,)
