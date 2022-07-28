import pathlib

BASE_DIR = str(pathlib.Path(__file__).parent.resolve())
DYNAMIC_VARIABLES_FILE_PATH = pathlib.Path(__file__).parent.resolve().joinpath("dynamic_variables.json")

managed_languages_DEEPL = {
    "FRENCH": "FR",
    "ENGLISH": "EN-GB",
}
