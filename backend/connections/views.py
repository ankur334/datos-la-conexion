from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from connections.exceptions import UnsupportedSerializerException
from connections.serializers import (
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
        serializer_klass = self.get_serializer_klass(self.request.data['connection_type'])
        serializer = serializer_klass(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
