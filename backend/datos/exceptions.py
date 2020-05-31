from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler

from connections.exceptions import ConnectionException


def process_validation_error(detail):
    message = ''
    for key, value in detail.items():
        if key == 'non_field_errors':
            message = value[0]
        else:
            temp = ''
            for items in value:
                temp = temp + items + ' '
                message = message + '{}: {}'.format(key, temp)

    return message


def custom_exception_handler(exc, context):
    """
    Custom Exception handler for DRF calls for overall app
    :param exc: Exception raised
    :param context: Context of the exception
    :return: Proper Error Response
    """
    response = exception_handler(exc, context)

    if isinstance(exc, ValidationError):
        if isinstance(exc.detail, dict):
            message = process_validation_error(exc.detail)
            response.status_code = 400
            response.data['message'] = message
        elif isinstance(exc.detail, list):
            response.status_code = 400
            response.data = {"message": exc.detail[0]}

        return response

    elif isinstance(exc, ConnectionException):
        if exc.status is not None:
            return Response(
                data={
                    "message": exc.message,
                    "params": exc.params if exc.params is not None else {}
                },
                status=exc.status
            )
        else:
            return Response(
                data={
                    "message": exc.message,
                    "params": exc.params if exc.params is not None else {}
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
