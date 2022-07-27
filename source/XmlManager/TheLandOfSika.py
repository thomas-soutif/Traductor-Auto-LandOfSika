import re

import lxml.etree as ET
from . import XmlManager
from source.Exceptions import CheckFileXMLException


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
        Get all the "strings" nodes
        :return:
        """
        return self.get_nodes("strings")

    def save_all_translate_nodes(self, nodes_string):
        """
        Save all the nodes "strings" to the xml file
        :param nodes_string:
        :return:
        """
        root = self.get_root()
        translate_nodes = self.get_all_translate_nodes()
        root.remove(translate_nodes)
        root.append(nodes_string)

    def get_text_translate_node(self, node) -> str:
        """
        Get the text content of a "string" node
        :param node:
        :return: The text of the node
        """
        return node.get("text")

    def set_text_translate_node(self, node, text) -> ET.Element:
        """
        Set the text content of a "string" node
        :param node:
        :param text:
        :return: The new node
        """
        node.set("text", text)
        return node

    def check_if_is_correct_translate_node(self, node) -> bool:
        """
        Check if the node is a valid "string" node
        :param node:
        :return: True if the node is valid
        """
        if not node.items() or not node.get("text"):
            return False
        return True

    def get_list_dynamic_variable(self) -> [str]:
        """
        Get a list of the dynamic variable in the xml file, for example {PLAYER.NAME} , they should not be translate directly
        :return: A list of string items
        """
        final_list = []
        for node in self.get_all_translate_nodes():
            match_result = self.get_dynamic_variable_of_node(node)
            if not match_result:
                continue
            for match in match_result:
                if match not in final_list:
                    final_list.append(match)

        return final_list


    def get_dynamic_variable_of_node(self,node):
        """
        Return a list of dynamic variable of the node, for example {PLAYER.NAME}, they should not be translate directly
        :param node:
        :return: A list of string items
        """
        text = self.get_text_translate_node(node)
        if not self.check_if_is_correct_translate_node(node):
            return None
        match_result = re.findall("\{(.*?)\}", text)
        return match_result