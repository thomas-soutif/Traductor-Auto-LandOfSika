import click
from source.XmlManager.TheLandOfSika import XmlManagerTheLandOfSika


@click.command(no_args_is_help=True)
@click.option('--file_path', default="", help='The XML File path to translate')
def run(file_path: str):
    if not file_path:
        raise Exception("You must pass a xml file as first argument")
    xml_manager = XmlManagerTheLandOfSika(file_path=file_path)
    for node in xml_manager.get_all_translate_nodes():
        if not xml_manager.check_if_is_correct_translate_node(node):
            continue
        xml_manager.set_text_translate_node(node, "ceci est un test")

    xml_manager.save_file(file_path.replace(".xml", "") + "COPY.xml")



if __name__ == "__main__":
    run()


