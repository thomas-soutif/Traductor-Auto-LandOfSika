import pathlib

BASE_DIR = str(pathlib.Path(__file__).parent.resolve())
DYNAMIC_VARIABLES_FILE_PATH = pathlib.Path(__file__).parent.resolve().joinpath("dynamic_variables.json")

managed_languages_DEEPL = [
    {
        "language": "BG",
        "name": "Bulgarian",
        "supports_formality": False
    },
    {
        "language": "CS",
        "name": "Czech",
        "supports_formality": False
    },
    {
        "language": "DA",
        "name": "Danish",
        "supports_formality": False
    },
    {
        "language": "DE",
        "name": "German",
        "supports_formality": True
    },
    {
        "language": "EL",
        "name": "Greek",
        "supports_formality": False
    },
    {
        "language": "EN-GB",
        "name": "English",
        "supports_formality": False
    },
    {
        "language": "ES",
        "name": "Spanish",
        "supports_formality": True
    },
    {
        "language": "ET",
        "name": "Estonian",
        "supports_formality": False
    },
    {
        "language": "FI",
        "name": "Finnish",
        "supports_formality": False
    },
    {
        "language": "FR",
        "name": "French",
        "supports_formality": True
    },
    {
        "language": "HU",
        "name": "Hungarian",
        "supports_formality": False
    },
    {
        "language": "ID",
        "name": "Indonesian",
        "supports_formality": False
    },
    {
        "language": "IT",
        "name": "Italian",
        "supports_formality": True
    },
    {
        "language": "JA",
        "name": "Japanese",
        "supports_formality": False
    },
    {
        "language": "LT",
        "name": "Lithuanian",
        "supports_formality": False
    },
    {
        "language": "LV",
        "name": "Latvian",
        "supports_formality": False
    },
    {
        "language": "NL",
        "name": "Dutch",
        "supports_formality": True
    },
    {
        "language": "PL",
        "name": "Polish",
        "supports_formality": True
    },
    {
        "language": "PT-PT",
        "name": "Portuguese",
        "supports_formality": True
    },
    {
        "language": "RO",
        "name": "Romanian",
        "supports_formality": False
    },
    {
        "language": "RU",
        "name": "Russian",
        "supports_formality": True
    },
    {
        "language": "SK",
        "name": "Slovak",
        "supports_formality": False
    },
    {
        "language": "SL",
        "name": "Slovenian",
        "supports_formality": False
    },
    {
        "language": "TR",
        "name": "Turkish",
        "supports_formality": False
    },
    {
        "language": "SV",
        "name": "Swedish",
        "supports_formality": False
    },
    {
        "language": "ZH",
        "name": "Chinese",
        "supports_formality": False
    }
]
