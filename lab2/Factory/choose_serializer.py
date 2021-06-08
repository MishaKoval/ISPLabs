from Serializers.my_pickle import PickleParser
from Serializers.my_json import JsonParser


class ChooseSerializer:

    @staticmethod
    def choose(info):
        if info == "json":
            return JsonParser
        elif info == "pickle":
            return PickleParser
        else:
            raise Exception('Incorrect type!')
