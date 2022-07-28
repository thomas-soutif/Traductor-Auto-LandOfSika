class CheckFileXMLException(Exception):
    def __init__(self, *args, file_path: str, manager_name: str, **kwargs):
        self.file_path = file_path
        self.manager_name = manager_name
        super().__init__(*args, **kwargs)


class DeepLAuthKeyNotSetException(Exception):
    ...

class DeepLAuthKeyWrongException(Exception):
    ...

class DeepLLanguageTargetNotManagedException(Exception):
    ...