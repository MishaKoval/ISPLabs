import unittest
from Serializers.SerializerFactory import *
from Tests.Objects import *


class MySerializersTest(unittest.TestCase):
    def setUp(self):
        self.json_serializer = Factory.get_instance(SerializeEnum.JSON)
        self.pickle_serializer = Factory.get_instance(SerializeEnum.PICKLE)
        self.yaml_serializer = Factory.get_instance(SerializeEnum.YAML)
        self.toml_serializer = Factory.get_instance(SerializeEnum.TOML)

        self.obj = Objects()

    def test_list(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(self.obj.list))
        pickle_obj = self.pickle_serializer.loads(self.pickle_serializer.dumps(self.obj.list))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(self.obj.list))

        self.assertEqual(json_obj, self.obj.list)
        self.assertEqual(pickle_obj, self.obj.list)
        self.assertEqual(yaml_obj, self.obj.list)

    def test_obj_json(self):
        self.fp = './Files/file.json'
        self.json_serializer.dump(test_obj, self.fp)
        t_obj = self.json_serializer.load(self.fp)
        self.assertEqual(t_obj.str, test_obj.str)

    def test_obj_pickle(self):
        self.fp = './Files/file.pickle'
        self.pickle_serializer.dump(test_obj, self.fp)
        t_obj = self.pickle_serializer.load(self.fp)
        self.assertEqual(t_obj.str, test_obj.str)

    def test_obj_toml(self):
        self.fp = './Files/file.toml'
        self.toml_serializer.dump(test_obj, self.fp)
        t_obj = self.toml_serializer.load(self.fp)
        self.assertEqual(t_obj.str, test_obj.str)

    def test_obj_yaml(self):
        self.fp = './Files/file.yaml'
        self.yaml_serializer.dump(test_obj, self.fp)
        t_obj = self.yaml_serializer.load(self.fp)
        self.assertEqual(t_obj.str, test_obj.str)

    def test_function_json(self):
        self.fp = './Files/file.json'
        self.json_serializer.dump(function, self.fp)
        test_func = self.json_serializer.load(self.fp)
        self.assertEqual(test_func(), function())

    def test_function_pickle(self):
        self.fp = './Files/file.pickle'
        self.pickle_serializer.dump(function, self.fp)
        test_func = self.pickle_serializer.load(self.fp)
        self.assertEqual(test_func(), function())

    def test_function_toml(self):
        self.fp = './Files/file.toml'
        self.toml_serializer.dump(factorial, self.fp)
        test_func = self.toml_serializer.load(self.fp)
        self.assertEqual(test_func(5), factorial(5))

    def test_function_yaml(self):
        self.fp = './Files/file.yaml'
        self.yaml_serializer.dump(function, self.fp)
        test_func = self.yaml_serializer.load(self.fp)
        self.assertEqual(test_func(), function())


if __name__ == "__main__":
    unittest.main()
