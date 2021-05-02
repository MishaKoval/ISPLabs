from Serializers.MyJsonSerializer import MyJsonSerializer
from Serializers.MyTomlSerializer import MyTomlSerializer
from Serializers.MyYamlSerializer import MyYamlSerializer
from Serializers.MyPickleSerializer import MyPickleSerializer
from enum import Enum


class SerializeEnum(Enum):
    JSON = 1
    TOML = 2
    YAML = 3
    PICKLE = 4


class Factory(object):
    @staticmethod
    def get_instance(serializer_type):
        if serializer_type is SerializeEnum.JSON:
            return MyJsonSerializer()
        elif serializer_type is SerializeEnum.TOML:
            return MyTomlSerializer()
        elif serializer_type is SerializeEnum.YAML:
            return MyYamlSerializer()
        elif serializer_type is SerializeEnum.PICKLE:
            return MyPickleSerializer()
        else:
            raise Exception('Error in serializer type!')
