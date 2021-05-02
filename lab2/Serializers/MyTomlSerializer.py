import  toml
from Serializers.MySerializer import MySerializer


class MyTomlSerializer(MySerializer):

    def dumps(self, obj):
        obj_dict = super().dumps(obj)
        if 'code' in obj_dict:
            for (key, value) in obj_dict['code'].items():
                if key == 'co_consts':
                    value = list(value)
                    value[value.index(None)] = 0
                    obj_dict['code'][key] = value

        return toml.dumps(obj_dict)

    def loads(self, toml_str):
        return super().loads(toml.loads(toml_str))