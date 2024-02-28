from rest_framework import serializers
from .models import Careers


class CareersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = "__all__"
        
    def update(self, instance, validated_data):
        if validated_data.get("username"):
            raise serializers.ValidationError({"username": "This field cannot be updated."})
            
        return super().update(instance, validated_data)