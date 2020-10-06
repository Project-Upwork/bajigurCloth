from rest_framework import generics, permissions
from createwish.models import Wish
from api._wish.creator.serializers import WishSerializer
from api._wish.permissions import IsAdminOrReadOnly, MemberAccessPermission


class WishList(generics.ListAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    permission_classes = (MemberAccessPermission,)


class WishCreate(generics.CreateAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    permission_classes = (MemberAccessPermission,)