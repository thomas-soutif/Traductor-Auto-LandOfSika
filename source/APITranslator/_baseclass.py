class APITranslator:

    def auth(self):
        raise NotImplementedError("API Translator => auh")

    def translate(self, text_to_translate: str):
        raise NotImplementedError("API Translator => translate ")

    def check_if_language_managed(self):
        raise NotImplementedError("API Translator => check_if_language_managed")

    def managed_languages(self):
        raise NotImplementedError("API Translator => managed_languages")

    def get_target_language_key(self):
        raise NotImplementedError("API Translator => get_target_language_key")

    def get_list_modules_api(self) -> [str]:
        """
        Return the list of the modules api avalaible for this project
        :return: A list of string
        """
        return ["DEEPL"]
    def get_module_api(self) -> str:
        """
        Return the module use in this class
        :return: A string
        """
        raise NotImplementedError("API Translator => get_module_api")