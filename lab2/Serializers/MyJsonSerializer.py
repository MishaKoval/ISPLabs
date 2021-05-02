import json
from Serializers.MySerializer import MySerializer


class MyJsonSerializer(MySerializer):

    def dumps(self, obj):
        return json.dumps(super().dumps(obj), indent=4)

    def loads(self, json_str):
        return super().loads(json.loads(json_str))