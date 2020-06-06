from rest_framework import serializers

from connections.exceptions import FileValidationException, ConnectionException
from connections.models import File
from connections.utils import get_extension_of_file


class FlatDataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

    def create(self, validated_data):
        """

        :param validated_data:
        :return:
        """
        print("Validated Data \n", validated_data)
        instance = File.objects.create(**validated_data)
        
        return instance


class DataBaseDataSourceSerializer(serializers.ModelSerializer):
    database_params = serializers.JSONField(required=False, write_only=True)


class CloudDataSourceSerializer(serializers.ModelSerializer):
    cloud_params = serializers.JSONField(required=False, write_only=True)
