import os

from django.conf import settings
from django.db.models.fields.files import FieldFile
from rest_framework.exceptions import ValidationError

from connections.exceptions import FileValidationException


def upload_location(instance, filename):
    """
    Util function to create upload path
    :param instance: data source instance
    :param filename: name of the file uploaded
    :return: str; path
    """
    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)

    location = os.path.join(settings.MEDIA_ROOT, 'uploads', filename)
    return location


def get_supported_type(file):
    """
    For now we only support .csv and .xlsx file.
    :param file:
    :return:
    """
    extension = os.path.splitext(file.name)[1]  # [0] returns path+filename
    valid_extensions = ['.csv', '.xlsx']
    if not extension.lower() in valid_extensions:
        raise ValidationError(f'Unsupported file extension {extension}.')


def get_maximum_size(file):
    """
    For now we only support file smaller than 250 MB of size.
    :param file:
    :return:
    """
    if file.size > 5000000000:
        raise ValidationError('Maximum size is exceeding 250MB')


def get_minimum_size(file):
    """
    We don't support blank file.
    :param file:
    :return:
    """
    if file.size == 0:
        raise ValidationError("This file is empty.")


def validate_file(file):
    """
    function for validating file which is being uploaded.
    For now: We support only csv and xlsx for now. File size should not be more than 250 MB and equal to 0 Bytes
    :param file:
    :return:
    """
    if isinstance(file, FieldFile):
        file = file.file
    try:
        _validations = {
            "supported_type": get_supported_type,
            "maximum_size": get_maximum_size,
            "minimum_size": get_minimum_size
        }
        for key in _validations:
            _validations[key](file)
    except Exception as e:
        raise FileValidationException(
            message=str(e),
            params={
                "info": str(e),
                "type": "client",
                "exception": "Exception"
            }
        )
