import configparser
from Serializers.MySerializer import MySerializer
from Serializers.SerializerFactory import Factory
from Serializers.SerializerFactory import SerializeEnum
from pathlib import Path
import argparse


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


def serialize(dest_format, path_file):
    serializer = gettype(dest_format)
    try:
        src_format = Path(path_file).suffix
        src_format = src_format.removeprefix('.')
        src_format = src_format.upper()
        if src_format == dest_format:
            return
        deserializer = gettype(src_format)
        abs_path = Path(path_file)
        loaded = deserializer.load(path_file)
        dest_format = '.' + dest_format
        dest_format = dest_format.lower()
        serializer.dump(loaded, Path(abs_path.parent, f"{abs_path.stem}{dest_format}"))
    except FileNotFoundError:
        print("wrong path or format")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--config", dest="config_file", help="Path for the configuration file")
    parser.add_argument("-f", "--format", dest="dest_format", help="New file format")
    parser.add_argument("-p", "--path", dest="path_file", help="Path for the input file")
    args = parser.parse_args()

    if args.config_file is not None:
        config = configparser.ConfigParser()
        try:
            config.read(args.config_file)
            serialize(config["settings"]["dest_format"], config["settings"]["path_file"])
        except KeyError:
            print("invalid file")
    else:
        if args.dest_format and args.path_file:
            serialize(args.dest_format, args.path_file)
        else:
            raise TypeError("invalid parameters")


main()
