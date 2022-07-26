from Exceptions.XmlManage.Exceptions_XmlManage import CheckFileXML
from XmlManage.XmlManager import XmlManager


class XmlManagerTheLandOfSika(XmlManager):
    manager_name = "TheLandOfSika"

    def __init__(self, file_path):
        XmlManager.__init__(self, file_path)

    def check_xml_file(self):
        if not self.get_nodes("strings"):
            raise CheckFileXML(file_path=self.file_path, manager_name=self.manager_name)
