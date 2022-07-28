import os

import deepl

from config import managed_languages_DEEPL
from . import APITranslator
from dotenv import load_dotenv

from ..Exceptions import DeepLAuthKeyNotSetException, DeepLAuthKeyWrongException, DeepLLanguageTargetNotManagedException


class DeepLTranslator(APITranslator):
    translator_object = None
    target_language_full = None

    def __init__(self, target_language_full: str):
        self.target_language_full = target_language_full
        self.auth()
        self.check_auth()
        self.check_if_language_managed()
        self.target_language_full = target_language_full

    def auth(self):
        """
        Load the KEY_DEEPL_API in the .env file to authentificate you on the DeepL API.
        :return:
        """
        load_dotenv()
        if not (os.getenv("KEY_DEEPL_API")):
            raise DeepLAuthKeyNotSetException(
                "The Auth key for DeepL was not found in the .env file, please set it as 'KEY_DEEPL_API' ")
        self.translator_object = deepl.Translator(os.getenv("KEY_DEEPL_API"))

    def translate(self, text_to_translate: str, source_language: str, target_language: str):
        """
        Translate a text with DeepL to the specified target language.
        :param text_to_translate:
        :param source_language:
        :param target_language:
        :return: The text translated
        """
        result = self.translator_object.translate_text(text_to_translate, target_lang=target_language)
        return result.text

    def check_auth(self):
        """
        Check if the authentification for the DeepL API is correct. For more information on how to setup it, visit the DeepL Api Website
        :return: An exeception if the check failed
        """
        try:
            self.translator_object.get_usage()
        except deepl.exceptions.AuthorizationException:
            raise DeepLAuthKeyWrongException("The authentification key set in the .env is wrong, please check it")
        except Exception as e:
            raise e

    def translate_to_french(self, text_to_translate):
        """
        Translate a text with DeepL to the French language
        :param text_to_translate:
        :return:
        """
        return self.translate(text_to_translate=text_to_translate, source_language="", target_language="FR")

    def managed_languages(self) -> dict:
        """
        Return a list of the languages managed by the module for DeepL. It can be configure in the config.py file
        :return: A dict that contains the language and his target_language named from the DeepL API point of view
        """
        return managed_languages_DEEPL

    def check_if_language_managed(self) -> None:
        """
        Check if the language target name (for example French) is managed by the module
        :param language_target_name:
        :return: raise of the language is not supported by the module, else None
        """
        if not self.managed_languages().get(self.target_language_full, None):
            raise DeepLLanguageTargetNotManagedException(
                f"The language {self.target_language_full} is not managed by the "
                f"DeepL Module. Please add it to the configuration file "
                f"'config.py' in the variable 'managed_languages_DEEPL'. The list of language managed is {list(self.managed_languages().keys())}")

    def get_target_language_key(self) -> str:
        """
        Get the key name of the target language key managed by the module. For example, the key of "French" is "FR"
        :param language_target_name:
        :return: The key
        """
        self.check_if_language_managed()
        return self.managed_languages().get(self.target_language_full)
