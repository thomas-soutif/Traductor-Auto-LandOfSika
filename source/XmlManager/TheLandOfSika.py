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

    def get_dynamic_variable_of_node(self, node):
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

    def set_dynamic_variable_for_node(self, node: ET.Element, variable: str, value: str):
        """
        Set the dynamic variable for a node
        Example :
             For the string "Hello {PLAYER.NAME}" with variable= PLAYER.NAME and value "JOHN", the result will be "Hello JOHN"
        :param node:
        :param variable:
        :param value:
        :return: The node with the text changed
        :
        """
        if variable == "SETTLEMENT":
            pass
        text = self.get_text_translate_node(node)
        accept_ponctuation = [",", ".", "?", "!", " "]
        variable_braket = "{" + variable + "}"
        pos_variable_bracket = text.find(variable_braket)
        if pos_variable_bracket > 0:
            if text[pos_variable_bracket - 1] not in accept_ponctuation:
                variable_braket_space = " {" + variable
            else:
                variable_braket_space = "{" + variable
            try:
                if pos_variable_bracket + 1 <= len(text) and text[
                    pos_variable_bracket + len(variable_braket)] not in accept_ponctuation:
                    variable_braket_space += "} "
            except IndexError:
                return node
            else:
                variable_braket_space += "}"
                text = text.replace(variable_braket, variable_braket_space)

        text = text.replace(variable_braket, value)
        return self.set_text_translate_node(node, text)

    def reverse_dynamic_variable_for_node(self, node: ET.Element, value: str, variable: str):
        """
        Reverse the action of set dynamic variable for the node
        Example:
            For the string "Hello JOHN" with value=JOHN and variable= PLAYER.NAME, the result will be "Hello {PLAYER.NAME}"
        :param node:
        :param value:
        :param variable:
        :return: The node with the text changed
        """
        text = self.get_text_translate_node(node)
        text = text.replace(value, "{" + variable + "}")
        return self.set_text_translate_node(node, text)

    def format_text_translate(self, text: str):
        """
        Replace the text with the right format for adapt to the xml format of the land of sika
        :param text:
        :return: The text format
        """

        return text.replace('"', "'")
