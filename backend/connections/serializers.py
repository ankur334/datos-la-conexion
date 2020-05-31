from rest_framework import serializers

from connections.exceptions import FileValidationException, ConnectionException
from connections.models import File


class FlatDataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

    def create(self, validated_data):
        """

        :param validated_data:
        :return:
        """

        return File.objects.create(**validated_data)


class DataBaseDataSourceSerializer(serializers.ModelSerializer):
    database_params = serializers.JSONField(required=False, write_only=True)


class CloudDataSourceSerializer(serializers.ModelSerializer):
    cloud_params = serializers.JSONField(required=False, write_only=True)
