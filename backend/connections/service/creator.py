import datetime
from string import Template

import psycopg2
from django.db import transaction

from connections.service.extractor import ExtractorFactory
from datos.utils import random_string


class DataCreator:
    def __init__(self, **payload):
        self._payload = payload
        self._connection = None

    def get_connection(self):
        if self._connection is not None and self._connection.closed == 0:
            return self._connection
        params = self._payload["destination_info"]
        host = params['HOST']
        database = params['DATABASE']
        username = params['USER']
        password = params['PASSWORD']
        port = int(params['PORT'])
        self._connection = psycopg2.connect(
            host=host, database=database, user=username, password=password, port=port,
        )

        return self._connection

    def _create_extract(self):
        """

        :return:
        """
        print("Calling extract")
        print("payload here\n", self._payload)
        print(self._payload.get("extract_type"))
        print(self._payload.get("source_info"))
        print(self._payload.get("source_info").get("request_data"))
        extractor = ExtractorFactory.get_extractor(
            extract_type=self._payload.get("extract_type"),
            connection_type=self._payload.get("source_info").get("request_data").get("connection_type")
        )
        print("Extractor ", extractor)
        extract = extractor(
            **self._payload.get("source_info")
        ).extract()
        return extract

    def _save_extract_in_storage_table(self):
        """

        :return:
        """
        print()

    def dump(self, file_path):
        """
        data into the table
        :return: {"status": "success"/ "failed", "message": "relevant message"}
        """
        with open(file_path, 'r') as f:
            # Notice that we don't need the `csv` module.
            try:
                start = datetime.datetime.now()
                cursor = self._connection.cursor()
                table_name = random_string(3)
                sql_statement = Template("""
                    COPY $table_name FROM STDIN WITH
                    CSV
                    HEADER
                    DELIMITER AS ','
                """).substitute(table_name=random_string(3))
                # print("Sql Statement ", sql_statement)
                cursor.copy_expert(sql_statement, f)
                cursor.close()
                self._connection.commit()

                time_elapsed = str(datetime.datetime.now() - start)
                return {
                    'name': table_name,
                    'status': 'success',
                    'message': 'Data dump successful.'
                }

            except Exception as e:

                return {
                    'status': 'failed',
                    'message': str(e)
                }

    def create(self):
        """
        Method for creating connection for file, Database and API.
        1). An atomic is necessary, so that even if this block encounters an error and fails
            the transactions in the finally block are not affected by it
        Steps: a). Create Extract
        """
        creation_successful = False
        try:
            with transaction.atomic():
                _extracts = self._create_extract()
                self._save_extract_in_storage_table()
                self.get_connection()
                self.dump(_extracts["file_info"]["extract_path"])
                return _extracts
        except:
            print()
