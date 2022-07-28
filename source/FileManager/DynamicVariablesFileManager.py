import json
import logging


class DynamicVariablesFileManager:
    file_path = None
    json_data = None

    def __init__(self, file_path):
        self.file_path = file_path
        self.load_json_data()

    def load_json_data(self):
        """
        Load the json data of dynamic variable file
        :return: The data , or None if nothing was found
        """
        try:
            file = open(self.file_path, "r").read()
        except FileNotFoundError:
            with open(self.file_path,"w") as f:
                f.write("{}")
                file = open(self.file_path, "r").read()
        try:
            json_data = json.loads(file)
            self.json_data = json_data
            return json_data
        except json.JSONDecodeError:
            logging.error("Could not read the dynamic_variables file because the content is not json type.")
            return None

    def write_json_data(self, json_data):
        """
        Write the json data to the dynamic variable file
        :param json_data:
        :return: True if it was write, else False
        """
        with open(self.file_path, "w") as outfile:
            json.dump(json_data, outfile)
        self.json_data = json_data
        return True

    def get_json_data(self):
        return self.json_data
