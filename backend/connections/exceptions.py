class ConnectionException(Exception):
    def __init__(self, message, params=None, status=None):
        self.message = message
        self.params = params
        self.status = status

    def __str__(self):
        return self.message


class UnsupportedSerializerException(ConnectionException):
    pass


class FileValidationException(ConnectionException):
    pass
