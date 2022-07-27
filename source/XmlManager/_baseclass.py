import io
import lxml.etree as ET
from io import BytesIO


class XmlManager:
    xml_object_parse: ET.ElementTree = None
    file_path: str = None

    def __init__(self, file_path: str):
        self.file_path = file_path
        self._register_all_namespaces()
        self._load_xml_from_file_path(self.file_path)

    def _register_all_namespaces(self):
        namespaces = dict([node for _, node in ET.iterparse(self.file_path, events=['start-ns'])])
        for ns in namespaces:
            ET.register_namespace(ns, namespaces[ns])

    def _load_xml_from_file_path(self, file_path):
        self.xml_object_parse = ET.parse(
            file_path
        )

    def get_root(self) -> ET.Element:
        """
        Get Root of this Tree
        :return: The Root of the tree
        """
        return self.xml_object_parse.getroot()

    def get_nodes(self, name) -> ET.Element:
        """
        Return the nodes specify by name
        :return:
        """
        return self.get_root().find(name)

    def save_file(self, path) -> io.BytesIO:
        """
        Save the xml file to the path specified
        :param path:
        :return: The plan file
        """
        self.xml_object_parse.write(path)

    def check_xml_file(self):
        """
        Verify if the xml file is the write one for the usecase
        :return:
        """
        raise NotImplementedError("Check xml file not implemented")
