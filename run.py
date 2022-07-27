import json
import logging
import os.path
from json import JSONDecodeError
from source.FileManager.DynamicVariablesFileManager import DynamicVariablesFileManager
import click

from config import BASE_DIR, DYNAMIC_VARIABLES_FILE_PATH
from source.XmlManager.TheLandOfSika import XmlManagerTheLandOfSika


@click.command(no_args_is_help=True)
@click.option('--file_path', default="", help='The XML File path to translate')
def run(file_path: str):
    if not file_path:
        raise Exception("You must pass a xml file as first argument")
    xml_manager = XmlManagerTheLandOfSika(file_path=file_path)
    # We check first if there is some dynamic variable to setup

    dynamic_variables = xml_manager.get_list_dynamic_variable()
    dynamic_variables_and_value_enter = {}
    if dynamic_variables:
        logging.warning(
            "Some dynamic variables have been found in the XML file, please fill for each one a word that fit it correctly, to be able to translate the sentence. You can left it empty and the sentence associated will be ignored and not translated.")
        print("\n")
        dynamic_variables_and_value_enter: dict = {}
        for variable in dynamic_variables:
            print(f"{variable} ==> ")
            value_enter_by_user = input()
            dynamic_variables_and_value_enter.update({variable: value_enter_by_user})

        #We save to a file the values, to be used again
        file_manager = DynamicVariablesFileManager(file_path=DYNAMIC_VARIABLES_FILE_PATH)
        json_data = file_manager.get_json_data()
        if not json_data:
            json_data ={}
        json_data.update(dynamic_variables_and_value_enter)
        file_manager.write_json_data(json_data)

    for node in xml_manager.get_all_translate_nodes():
        if not xml_manager.check_if_is_correct_translate_node(node):
            continue
        xml_manager.set_text_translate_node(node, "ceci est un test")

    xml_manager.save_file(file_path.replace(".xml", "") + "COPY.xml")




if __name__ == "__main__":
    run()
