

import json

class JsonUtilities:
    @staticmethod
    def convert_string_to_json(string: str):
        """
        Converts a string to a JSON object
        :param string: string to convert
        :return: JSON object
        """
        try:
            return json.loads(string)
        except Exception as e:
            print(e)
            raise e