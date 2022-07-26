class CheckFileXML(Exception):
    def __init__(self, *args, file_path: str,manager_name : str, **kwargs):
        self.file_path = file_path
        self.manager_name = manager_name
        super(CheckFileXML, self).__init__(*args, **kwargs)