from Exceptions.XmlManage.Exceptions_XmlManage import CheckFileXMLException
from XmlManage.XmlManager import XmlManager


class XmlManagerTheLandOfSika(XmlManager):
    manager_name = "TheLandOfSika"

    def __init__(self, file_path):
        XmlManager.__init__(self, file_path)
        self.check_xml_file()


    def check_xml_file(self):
        if not self.get_nodes("strings"):
            raise CheckFileXMLException(f"Le fichier xml {self.file_path} n'est pas reconnue par le manager {self.manager_name}", file_path=self.file_path, manager_name=self.manager_name)
