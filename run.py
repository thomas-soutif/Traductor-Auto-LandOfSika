import logging

import click
from source.XmlManager.TheLandOfSika import XmlManagerTheLandOfSika


@click.command(no_args_is_help=True)
@click.option('--file_path', default="", help='The XML File path to translate')
def run(file_path: str):
    if not file_path:
        raise Exception("You must pass a xml file as first argument")
    xml_manager = XmlManagerTheLandOfSika(file_path=file_path)
    # We check first if there is some dynamic variable to setup

    dynamic_variables = xml_manager.get_list_dynamic_variable()
    dynamic_variables_and_value_enter = None
    if dynamic_variables:
        logging.warning(
            "Some dynamic variables have been found in the XML file, please fill for each one a word that fit it correctly, to be able to translate the sentence. You can left it empty and the sentence associated will be ignored and not translated.")
        print("\n")
        dynamic_variables_and_value_enter: dict = {}
        for variable in dynamic_variables:
            print(f"{variable} ==> ")
            value_enter_by_user = input()
            dynamic_variables_and_value_enter.update({variable: value_enter_by_user})

    print(dynamic_variables_and_value_enter)
    exit()
    for node in xml_manager.get_all_translate_nodes():
        if not xml_manager.check_if_is_correct_translate_node(node):
            continue
        xml_manager.set_text_translate_node(node, "ceci est un test")

    xml_manager.save_file(file_path.replace(".xml", "") + "COPY.xml")


if __name__ == "__main__":
    run()
