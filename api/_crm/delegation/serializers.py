from rest_framework import serializers
from simplycrm.models import Staff

class DelegationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Staff
        fields = "__all__"