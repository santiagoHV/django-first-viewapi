from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """serializa un campo para probar la API"""

    name = serializers.CharField(max_length=10)