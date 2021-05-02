import yaml
from Serializers.MySerializer import MySerializer


class MyYamlSerializer(MySerializer):

    def dumps(self, obj):
        return yaml.dump(super().dumps(obj))

    def loads(self, yaml_str):
        return super().loads(yaml.unsafe_load(yaml_str))