import os
import shutil

from django.conf import settings

from connections.serializers import FlatDataSourceSerializer
from connections.utils import get_extension_of_file
from datos.utils import random_string


class FLATCSVExtractor:
    def __init__(self, **kwargs):
        self._request_data = kwargs.get("request_data")

    def _create_file_instance(self):
        print("Calling Connection")
        print()
        file = self._request_data["file"][0]
        file_name = file.name

        serializer_input = {
            "file": file,
            "name": file_name,
            "display_name": file.name,
            "type": get_extension_of_file(file.name)
        }
        print("Serializer Input \n", serializer_input)
        serializer = FlatDataSourceSerializer(data=serializer_input)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            return instance

    @staticmethod
    def _create_extract_directory():
        flat_file_extract_path = os.path.join(settings.MEDIA_ROOT, 'flat_file_extract')
        if not os.path.exists(flat_file_extract_path):
            os.makedirs(flat_file_extract_path)
        return flat_file_extract_path

    def extract(self):
        """
        In this function we will try to First create connection with file then
        :return:
        """

        file_instance = self._create_file_instance()
        flat_file_extract_path = self._create_extract_directory()
        filename, extension, file_path = file_instance.name, file_instance.type, file_instance.file.path
        new_file_location = os.path.join(
            flat_file_extract_path, filename + random_string() + "_extracted_files"
        )
        if not os.path.exists(new_file_location):
            os.makedirs(new_file_location)
        print("\n", new_file_location)
        shutil.copy(file_path, new_file_location)
        return {
            "file_info": {
                "extract_path": new_file_location
            }
        }
