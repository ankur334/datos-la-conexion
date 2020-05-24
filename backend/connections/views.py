from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class DataSourceAPIView(APIView):
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
