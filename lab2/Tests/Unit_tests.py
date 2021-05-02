import unittest
import sys

sys.path.insert(0, 'D:\PROJECTS\Python\Lab2\Serializers')

from Serializers.SerializerFactory import *
from Tests.Objects import *


class MySerializersTest(unittest.TestCase):
    def __init__(self, method):
        super().__init__(method)
        self.json_serializer = Factory.get_instance(SerializeEnum.JSON)
        self.pickle_serializer = Factory.get_instance(SerializeEnum.PICKLE)
        self.yaml_serializer = Factory.get_instance(SerializeEnum.YAML)
        self.toml_serializer = Factory.get_instance(SerializeEnum.TOML)

    def test_list(self):
        self.obj = Objects()
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(self.obj.list))
        pickle_obj = self.pickle_serializer.loads(self.pickle_serializer.dumps(self.obj.list))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(self.obj.list))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(self.obj.list))

        self.assertEqual(json_obj, self.obj.list)
        self.assertEqual(pickle_obj, self.obj.list)
        self.assertEqual(yaml_obj, self.obj.list)
        self.assertEqual(toml_obj, self.obj.list)
