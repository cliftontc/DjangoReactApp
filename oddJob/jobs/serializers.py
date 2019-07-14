from rest_framework import serializers
from jobs.models import Job
#job serializer
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
    