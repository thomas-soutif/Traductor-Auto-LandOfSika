from source.Exceptions.XmlManage.Exceptions_XmlManage import CheckFileXMLException
from source.XmlManage.XmlManager import XmlManager
import xml.etree.ElementTree as ET


class XmlManagerTheLandOfSika(XmlManager):
    manager_name = "TheLandOfSika"

    def __init__(self, file_path):
        XmlManager.__init__(self, file_path)
        self.check_xml_file()

    def check_xml_file(self):
        """
        Check if the xml file is the good one for the manager
        :return:
        """
        if not self.get_all_translate_nodes():
            raise CheckFileXMLException(
                f"Le fichier xml {self.file_path} n'est pas reconnue par le manager {self.manager_name}",
                file_path=self.file_path, manager_name=self.manager_name)

    def get_all_translate_nodes(self) -> ET.Element:
        """
        Get all the strings nodes
        :return:
        """
        return self.get_nodes("strings")

    def save_all_translate_nodes(self, nodes_string):
        """
        Save all the nodes strings to the xml file
        :param nodes_string:
        :return:
        """
        root = self.get_root()
        translate_nodes = self.get_all_translate_nodes()
        root.remove(translate_nodes)
        root.append(nodes_string)

    def get_text_translate_node(self, node) -> str:
        """
        Get the text content of a string node
        :param node:
        :return: The text of the node
        """
        return node.get("text")

    def set_text_translate_node(self, node, text) -> ET.Element:
        """
        Set the text content of a string node
        :param node:
        :param text:
        :return: The new node
        """
        node.set("text", text)
        return node
