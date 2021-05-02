import pickle
from Serializers.MySerializer import MySerializer


class MyPickleSerializer(MySerializer):

    def dump(self, obj, f_path):
        with open(f_path, 'wb') as file:
            pickle.dump(obj, file)

    def dumps(self, py_object):
        return pickle.dumps(super().dumps(py_object))

    def load(self, f_path):
        with open(f_path, 'rb') as file:
            obj = pickle.load(file)

        return obj

    def loads(self, pickle_str):
        return super().loads(pickle.loads(pickle_str))