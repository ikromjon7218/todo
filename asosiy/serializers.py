from rest_framework import serializers
from django.core.exceptions import ValidationError
import datetime
from .models import *
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

    def validate_sarlavha(self, value):
        if len(value) > 20:
            print(value)
            raise serializers.ValidationError("Sarlavha 20 ta belgidan ko'p bo'lishi mumkin emas.")
        print(value, 1)
        return value

    def validate_batafsil(self, value):
        if value:
            if len(value) > 300:
                raise ValidationError("Batafsil ma'lumot 300 ta belgidan oshmasligi kerak")
            return value

    def validate_zarurlik(self, value):
        if value:
            if value not in ('shart', 'foydali', 'hayot_mamot', 'qiziqishga'):
                raise ValidationError(
                    "Zarurlik jadvali qiyati (shart, foydali, hayot_mamot, qiziqishga) so'zlaridan biri bo'lishi kerak.")
        return value