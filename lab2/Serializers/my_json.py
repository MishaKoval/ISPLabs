from Serializers.serializer import dumps as _dumps
from Serializers.serializer import dump as _dump
from Serializers.serializer import loads as _loads
from Serializers.serializer import load as _load


class JsonParser:

    def dumps(self, value_indent, value_sort):
        return _dumps(self, value_indent, value_sort)

    def loads(self):
        return _loads(self)

    def dump(self, fp, value_indent, value_sort):
        return _dump(self, fp, value_indent, value_sort)

    def load(self):
        return _load(self)
