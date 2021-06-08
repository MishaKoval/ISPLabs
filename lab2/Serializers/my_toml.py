from Serializers.serializer import dumps as _dumps
from Serializers.serializer import dump as _dump
from Serializers.serializer import loads as _loads
from Serializers.serializer import load as _load
import toml


class TomlParser:
    def dump(self, save_file_path, obj):
        with open(save_file_path, 'w') as file:
            toml.dump(_dump(obj), file)

    def dumps(self, obj):
        return toml.dumps(_dump(obj))

    def load(self, load_file_path):
        with open(load_file_path, 'r') as file:
            return _load(toml.loads(file.read()))

    def loads(self, toml_string):
        return _loads(toml.loads(toml_string))