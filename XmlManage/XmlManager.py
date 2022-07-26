import xml.etree.ElementTree as ET
class XmlManager:


    xml_object_parse : ET.ElementTree = None
    file_path : str = None

    def __init__(self, file_path: str):
        self.file_path = file_path
        self._load_xml_from_file_path(self.file_path)

    def _load_xml_from_file_path(self,file_path):
        self.xml_object_parse = ET.parse(
            file_path
        )
    def write_xml_to_file_path(self):
        pass



    def get_root(self) -> ET.Element:
        """
        Get Root of this Tree
        :return: The Root of the tree
        """
        return self.xml_object_parse.getroot()

    def get_nodes(self, name):
        """
        Return the nodes specify by name
        :return:
        """
        self.get_root().find(name)


    def check_xml_file(self):
        """
        Verify if the xml file is the write one for the usecase
        :return:
        """
        raise "Check xml file not implemented"