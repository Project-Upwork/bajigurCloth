from rest_framework import serializers
from simplycrm.models import JobDesk

class JobDeskSerializer(serializers.ModelSerializer):
    class Meta: 
        model = JobDesk
        fields = "__all__"