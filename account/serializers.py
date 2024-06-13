from rest_framework import serializers


class AccountSerializer(serializers.Serializers):
    account_number = serializers.CharField(max_length=10)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    balance = serializers.DecimalField(max_digits=6, decimal_places=2)
    account_type = serializers.CharField(max_length=10)