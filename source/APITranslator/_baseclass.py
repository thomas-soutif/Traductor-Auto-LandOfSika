class APITranslator:

    def auth(self):
        raise NotImplementedError("API Translator => auh not implemented")

    def translate(self, text_to_translate: str, source_language: str, target_language: str):
        raise NotImplementedError("API Translator => translate not implemented")
