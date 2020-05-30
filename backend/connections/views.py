from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.connections.exceptions import UnsupportedSerializerException
from backend.connections.serializers import (
    FlatDataSourceSerializer, DataBaseDataSourceSerializer,
    CloudDataSourceSerializer
)


class DataSourceAPIView(APIView):

    @staticmethod
    def get_serializer_klass(connection_type):
        """
        This is getter for getting serializer class.
        :return:
        """
        try:
            connection_type = {
                "FLAT": FlatDataSourceSerializer,
                "DATABASE": DataBaseDataSourceSerializer,
                "CLOUD": CloudDataSourceSerializer,
            }
            return connection_type[str(connection_type).upper()]
        except KeyError as e:
            raise UnsupportedSerializerException(
                message=str(e),
                params={
                    "info": str(e),
                    "type": "client",
                    "exception": "KeyError"
                }
            )

    def get(self, request):
        return Response(
            data="Data-source get method worked perfectly",
            status=status.HTTP_200_OK
        )

    def post(self, request):

        return Response(
            data="Data-source POST method worked perfectly",
            status=status.HTTP_200_OK
        )

    def put(self, request):
        return Response(
            data="Data-source PUT method worked perfectly",
            status=status.HTTP_200_OK
        )

    def delete(self, request):
        return Response(
            data="Data-source DELETE method worked perfectly",
            status=status.HTTP_200_OK
        )
