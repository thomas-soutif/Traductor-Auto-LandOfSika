class APITranslator:

    def auth(self):
        raise NotImplementedError("API Translator => auh")

    def translate(self, text_to_translate: str, source_language: str, target_language: str):
        raise NotImplementedError("API Translator => translate ")

    def check_if_language_managed(self, language_target_name):
        raise NotImplementedError("API Translator => check_if_language_managed")

    def managed_languages(self):
        raise NotImplementedError("API Translator => managed_languages")

    def get_target_language_key(self):
        raise NotImplementedError("API Translator => get_target_language_key")
