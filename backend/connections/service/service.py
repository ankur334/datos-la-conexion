from django.conf import settings

from connections.service.creator import DataCreator


class DataService:
    def __init__(self, **request_data):
        self._request_data = request_data

    def get_payload(self):
        """

        :return:
        """
        _payload = {
            "source_info": {
                "request_data": self._request_data
            },
            "destination_info": settings.DATABASES["data"],
            "extract_type": settings.EXTRACT_TYPE
        }
        return _payload

    def process_data_source(self):
        """

        :return:
        """
        payload = self.get_payload()
        data_source = DataCreator(**payload).create()
        return data_source
