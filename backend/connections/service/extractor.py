from connections.service.files.extractor import FLATCSVExtractor


class ExtractorFactory:

    @staticmethod
    def get_extractor(extract_type, connection_type):
        """
        Factory driver method which will help me to get required klass
        :return:
        """
        print("Calling get extractor")
        print("extract_type ", extract_type)
        print("Connection Type ", connection_type)
        if isinstance(connection_type, list):
            connection_type = connection_type[0]
        print("extract_type ", extract_type)
        print("Connection Type ", connection_type)
        if extract_type.upper() == "CSV":
            connection_type = connection_type.upper()
            if connection_type == "FLAT":
                return FLATCSVExtractor
            elif connection_type == "DATABASE":
                print()
            elif connection_type == "CLOUD":
                print()
            else:
                raise NotImplementedError(
                    "For now, we only support FLAT, DATABASE, CLOUD"
                )
        else:
            raise NotImplementedError(
                "For now we only support CSV as extract files."
            )