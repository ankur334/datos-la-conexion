from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from connections.exceptions import UnsupportedSerializerException, ConnectionException
from connections.serializers import (
    FlatDataSourceSerializer, DataBaseDataSourceSerializer,
    CloudDataSourceSerializer
)
from connections.utils import get_extension_of_file


class DataSourceAPIView(APIView):

    @staticmethod
    def get_payload(request_data):
        """

        :param request_data:
        :return:
        """
        if request_data['connection_type'].upper() == 'FLAT':
            request_data["name"] = request_data['file'].name
            request_data["display_name"] = request_data['file'].name
            request_data["type"] = get_extension_of_file(request_data["name"])
        return request_data

    @staticmethod
    def get_serializer_klass(connection_type):
        """
        This is getter for getting serializer class.
        :return:
        """
        print("connection_type", connection_type)
        print("type ", type(connection_type))
        try:
            serializer_klass = {
                "FLAT": FlatDataSourceSerializer,
                "DATABASE": DataBaseDataSourceSerializer,
                "CLOUD": CloudDataSourceSerializer,
            }
            return serializer_klass[f"{connection_type}"]
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
        parser_class = (FileUploadParser,)  # FileUploadParser parses raw file upload content.

        payload = self.get_payload(request.data)
        serializer_klass = self.get_serializer_klass(self.request.data['connection_type'])
        serializer = serializer_klass(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            raise ConnectionException(
                message=serializer.errors,
                params={
                    "info": serializer.errors,
                    "type": "server"
                }
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
