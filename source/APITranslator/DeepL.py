import os

import deepl

from . import APITranslator
from dotenv import load_dotenv

from ..Exceptions import DeepLAuthKeyNotSetException, DeepLAuthKeyWrongException


class DeepLTranslator(APITranslator):
    translator_object = None

    def __init__(self):
        self.auth()
        self.check_auth()

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
