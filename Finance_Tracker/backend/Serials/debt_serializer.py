from rest_framework import serializers
from ..Models.debt_information import DebtModel

class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebtModel
        fields = '__all__'
        read_only_fields = ['user']