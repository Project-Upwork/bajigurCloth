from rest_framework import serializers
from createwish.models import Wish

class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields=("account", "title","image","pricing","date","note","order_date")