from Serializers.MyConverter import Converter
import inspect


class MySerializer:

    def __init__(self):
        self.__converter = Converter()

    def dump(self, obj, f_path):
        with open(f_path, 'w') as file:
            file.write(self.dumps(obj))

    def dumps(self, obj):
        if inspect.isfunction(obj):
            return self.__converter.function_dictionary(obj)
        else:
            return self.__converter.object_dictionary(obj)

    def load(self, f_path):
        with open(f_path, 'r') as file:
            return self.loads(file.read())

    def loads(self, obj_dict):
        if 'code' in obj_dict:
            return self.__converter.dictionary_function(obj_dict)
        else:
            return self.__converter.dictionary_object(obj_dict)
