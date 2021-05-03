from Serializers.MySerializer import MySerializer
from Serializers.SerializerFactory import Factory
from Serializers.SerializerFactory import SerializeEnum


def gettype(type):
    serializer = MySerializer()
    if type == 'JSON':
        serializer = Factory.get_instance(SerializeEnum.JSON)
    elif type == 'YAML':
        serializer = Factory.get_instance(SerializeEnum.YAML)
    elif type == 'PICKLE':
        serializer = Factory.get_instance(SerializeEnum.PICKLE)
    elif type == 'TOML':
        serializer = Factory.get_instance(SerializeEnum.TOML)
    else:
        raise Exception('Error in serializer type!')
    return serializer


def main():
    gettype("JSON").dump(gettype("TOML").load("./Files/file.toml"), "./Files/file.json")


if __name__ == '__main__':
    main()
