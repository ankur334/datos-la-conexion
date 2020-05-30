from rest_framework import serializers


class FlatDataSourceSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False, write_only=True)


class DataBaseDataSourceSerializer(serializers.ModelSerializer):
    database_params = serializers.JSONField(required=False, write_only=True)


class CloudDataSourceSerializer(serializers.ModelSerializer):
    cloud_params = serializers.JSONField(required=False, write_only=True)
