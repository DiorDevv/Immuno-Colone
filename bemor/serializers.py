from rest_framework import serializers
from .models import Jinsi


class JinsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jinsi
        fields = ['id', 'gender']

    def validate_gender(self, value):
        value = value.upper()
        if value not in ['M', 'F']:
            raise serializers.ValidationError("Jins faqatt 'M' yoki 'F' bo'lishi mumkin!")
        return value

    def create(self, validated_data):
        return Jinsi.objects.create(**validated_data)
