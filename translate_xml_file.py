import sys
import logging
from source.FileManager.DynamicVariablesFileManager import DynamicVariablesFileManager
import click

from gevent.pool import Pool
from config import DYNAMIC_VARIABLES_FILE_PATH
from source.XmlManager.TheLandOfSika import XmlManagerTheLandOfSika
from source.APITranslator.DeepL import DeepLTranslator


@click.command(no_args_is_help=True)
@click.option('--file_path', default="", help='The XML File path to translate')
@click.option('--module_api', default="DEEPL", help='The module API to use')
@click.option('--target_language', default="ENGLISH", help='The module API to use')
@click.option('--file_name_destination', default="",
              help='The full path destination of the file where write the new xml file ')
def run(file_path: str, module_api: str, target_language: str, file_name_destination: str):
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.getLogger("deepl").setLevel(logging.WARNING)
    if not file_path:
        raise Exception("You must specify the file_path argument")
    if not file_name_destination:
        file_name_destination = file_path.replace(".xml", "") + f"-COPY-TO-{target_language}.xml"
        # raise Exception("You must specify the file_name_destination argument")
    xml_manager = XmlManagerTheLandOfSika(file_path=file_path)
    logging.info(f"Try to translate the file {file_path} \n\n")
    if module_api == "DEEPL":
        translator_module = DeepLTranslator(target_language_full=target_language, source_language=None)
    else:
        raise Exception("The module_api specify is not implemented")
    # We check first if there is some dynamic variable to setup
    dynamic_variables = xml_manager.get_list_dynamic_variable()
    dynamic_variables_and_value_enter = {}
    if dynamic_variables:
        file_manager = DynamicVariablesFileManager(file_path=DYNAMIC_VARIABLES_FILE_PATH)
        dynamic_variables_of_file = file_manager.get_json_data()
        logging.warning(
            "Some dynamic variables have been found in the XML file, please fill for each one a word that fit it correctly, to be able to translate the sentence. You can left it empty and the sentence associated will be ignored and not translated.")

        if dynamic_variables_of_file:

            use_config_data = False
            logging.info(
                "A configuration file have been found for the dynamic variable, would you like to use it to automatically fill the translation ?(By Default No) [Yes, No]")
            value_user = input()
            if value_user.lower() == "yes":
                use_config_data = True
            elif value_user.lower() == "no":
                use_config_data = False
            else:
                logging.info("We was waiting for Yes or No, use of the default value (No)")
            if use_config_data:
                new_dynamic_variables_to_set = []
                for key in dynamic_variables:
                    if not dynamic_variables_of_file.get(key):
                        new_dynamic_variables_to_set.append(key)
            else:
                new_dynamic_variables_to_set = dynamic_variables
        else:
            new_dynamic_variables_to_set = dynamic_variables
        if new_dynamic_variables_to_set:
            dynamic_variables_and_value_enter: dict = user_input_dynamic_variable(new_dynamic_variables_to_set)

        # We save to a file the values, to be used again

        if not dynamic_variables_of_file:
            dynamic_variables_of_file = {}
        dynamic_variables_of_file.update(dynamic_variables_and_value_enter)
        file_manager.write_json_data(dynamic_variables_of_file)

    logging.info("\n Start to translate to your language")
    CONCURRENCY = 10
    pool = Pool(CONCURRENCY)
    threads = [pool.spawn(multithreading_translate_node, xml_manager, translator_module, node) for node in
               xml_manager.get_all_translate_nodes()]
    pool.join()
    xml_manager.save_file(file_name_destination)
    logging.info(f"New XML file generate to : {file_name_destination}")


def user_input_dynamic_variable(dynamic_variables) -> dict:
    dynamic_variables_and_value_enter = {}
    for variable in dynamic_variables:
        print(f"{variable} ==> ")
        value_enter_by_user = input()
        dynamic_variables_and_value_enter.update({variable: value_enter_by_user})

    return dynamic_variables_and_value_enter


def multithreading_translate_node(xml_manager, module_traductor, node):
    if not xml_manager.check_if_is_correct_translate_node(node):
        return node
    list_dynamic_variable_node = xml_manager.get_dynamic_variable_of_node(node)
    if list_dynamic_variable_node:
        file_manager = DynamicVariablesFileManager(file_path=DYNAMIC_VARIABLES_FILE_PATH)
        dynamic_variables_of_file_json = file_manager.get_json_data()
        all_key_found = True
        for key in list_dynamic_variable_node:
            if not dynamic_variables_of_file_json.get(key):
                # We don't have the equivalent for the dynamic variable, cannot translate because it will not be accurage, ignore
                logging.warning(
                    f"Could not translate  the text because the dynamic variable {key} was not set : {xml_manager.get_text_translate_node(node)}")
                all_key_found = False
                break
            node = xml_manager.set_dynamic_variable_for_node(node=node, variable=key,
                                                             value=dynamic_variables_of_file_json.get(key))
        if not all_key_found:
            return node
    # translate
    translate_text = module_traductor.translate(xml_manager.get_text_translate_node(node))
    # format the text
    translate_text = xml_manager.format_text_translate(translate_text)
    node = xml_manager.set_text_translate_node(node, translate_text)
    # not implemented yet

    # reverse the dynamic variable replacement
    if list_dynamic_variable_node:
        file_manager = DynamicVariablesFileManager(file_path=DYNAMIC_VARIABLES_FILE_PATH)
        dynamic_variables_of_file_json = file_manager.get_json_data()
        for key in list_dynamic_variable_node:
            node = xml_manager.reverse_dynamic_variable_for_node(node=node,
                                                                 value=dynamic_variables_of_file_json.get(key),
                                                                 variable=key)
    return node


if __name__ == "__main__":
    run()
