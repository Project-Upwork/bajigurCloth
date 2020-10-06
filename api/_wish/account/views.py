from rest_framework import generics, permissions
from createwish.models import Account
from api._wish.account.serializers import AccountSerializer
from api._wish.permissions import IsAdminOrReadOnly, MemberAccessPermission

class AccountList(generics.ListCreateAPIView):
    queryset =Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAdminOrReadOnly,)

