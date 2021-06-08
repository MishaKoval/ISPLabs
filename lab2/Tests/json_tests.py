import unittest
import Tests.tests as tests
from Serializers import serializer


def converter(obj):
    return serializer.loads(serializer.dumps(obj))


class TestSerializer(unittest.TestCase):

    def __init__(self, method_name):
        super().__init__(method_name)

    def test_empty_object(self):
        objects = tests.objects
        self.assertEqual(objects, converter(objects))

    def test_simple_string(self):
        objects = tests.string
        self.assertEqual(objects, converter(objects))

    def test_simple_obj_1(self):
        objects = tests.t1
        self.assertEqual(objects, converter(objects))

    def test_simple_obj_2(self):
        objects = tests.t2
        self.assertEqual(objects, converter(objects))

    def test_simple_obj_3(self):
        objects = tests.t3
        self.assertEqual(objects, converter(objects))

    def test_simple_func(self):
        objects = tests.simple_func
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(), converter(objects)())

    def test_recursion_func(self):
        objects = tests.simple_recursion
        self.assertEqual(objects.__code__, converter(objects.__code__))
        try:
            converter(objects)()
        except RecursionError:
            pass

    def test_cycle_recursion_func(self):
        objects = tests.double_func_recursion_2
        self.assertEqual(objects.__code__, converter(objects.__code__))
        try:
            converter(objects)()
        except RecursionError:
            pass

    def test_func_with_globals_and_builtins(self):
        objects = tests.func_with_globals_and_builtins
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(), converter(objects)())

    def test_func_in_func(self):
        objects = tests.func_in_func
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(2, 3, 4), converter(objects)(2, 3, 4))

    def test_func_with_defaults(self):
        objects = tests.func_with_defaults
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(), converter(objects)())

    def test_tuple_returner(self):
        objects = tests.tuple_returner
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(2, 3, 4, 5), converter(objects)(2, 3, 4, 5))

    def test_set_returner(self):
        objects = tests.set_returner
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(2, 3, 4, 5), converter(objects)(2, 3, 4, 5))

    def test_func_with_args_sum(self):
        objects = tests.func_with_args_sum
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(2, 3, 4, 5), converter(objects)(2, 3, 4, 5))

    def test_func_with_args_d(self):
        objects = tests.func_with_args_d
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(a=4, b=3), converter(objects)(a=4, b=3))

    def test_decorator(self):

        def test_func():
            return 'hh'

        objects = tests.counter
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(test_func)(), converter(objects)(test_func)())

    # def test_check_decorator(self):
    #     objects = tests.check_decorator
    #     self.assertEqual(objects.__code__, converter(objects.__code__))
    #     self.assertEqual(objects(), converter(objects)())

    def test_simplified_defaults(self):
        objects = tests.p
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects()(), converter(objects)()())

    def test_simple_lambda(self):
        objects = tests.simplelambda
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(3), converter(objects)(3))

    def test_lambda_in_lambda(self):
        objects = tests.lambda_in_lambda
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(3), converter(objects)(3))

    def test_lambda_in_function(self):
        objects = tests.lambda_in_function
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(3), converter(objects)(3))

    def test_Empty_cls(self):
        objects = tests.Empty_cls
        converter(objects)()
        for i in objects().__dict__:
            self.assertEqual(getattr(objects(), i), getattr(converter(objects)(), i))

    # def test_Cls_with_inheritance(self):
    #     objects = tests.Simple_cls
    #     converter(objects)(5, 6)
    #     for i in objects(5, 6).__dict__:
    #         self.assertEqual(getattr(objects(2, 3), i), getattr(converter(objects)(2, 3), i))

    def test_Cls_with_staticmethod(self):
        objects = tests.Cls_with_staticmethod
        converter(objects)()
        for i in objects().__dict__:
            self.assertEqual(getattr(objects(), i), getattr(converter(objects)(), i))

    def test_Cls_with_classmethod(self):
        objects = tests.Cls_with_classmethod
        converter(objects)()
        for i in objects().__dict__:
            self.assertEqual(getattr(objects(), i), getattr(converter(objects)(), i))

    def test_Inherited_cls(self):
        objects = tests.Inherited_cls
        converter(objects)()
        for i in objects().__dict__:
            self.assertEqual(getattr(objects(), i), getattr(converter(objects)(), i))

    def test_Cls_with_class_and_static_methods(self):
        objects = tests.B
        converter(objects)()
        for i in objects().__dict__:
            self.assertEqual(getattr(objects(), i), getattr(converter(objects)(), i))
