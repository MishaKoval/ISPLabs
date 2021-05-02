import inspect
from collections import namedtuple
from types import FunctionType, CodeType
import builtins


class Converter:

    @staticmethod
    def __is_default(obj):
        return type(obj) in [int, float, str, bool, type(None)]

    def object_dictionary(self, obj):
        if self.__is_default(obj):
            return obj
        elif isinstance(obj, list):
            lst = list()
            for item in obj:
                lst.append(self.object_dictionary(item))
            return lst
        elif isinstance(obj, dict):
            return self.__to_dictionary(obj)
        else:
            return self.__to_dictionary(obj.__dict__)

    def __to_dictionary(self, dict_obj):
        obj_dict = dict()
        for (key, value) in dict_obj.items():
            if self.__is_default(value):
                obj_dict[key] = value
            else:
                obj_dict[key] = self.__to_dictionary(value)

        return obj_dict

    def dictionary_object(self, dict_obj):
        if self.__is_default(dict_obj):
            return dict_obj
        elif isinstance(dict_obj, list):
            lst = list()
            for item in dict_obj:
                lst.append(self.object_dictionary(item))
            return lst

        else:
            temp = dict()
            for (key, value) in dict_obj.items():
                if not self.__is_default(value):
                    temp[key] = self.object_dictionary(value)
                else:
                    temp[key] = value

        return namedtuple('object', temp.keys())(*temp.values())

    def function_dictionary(self, func_obj):
        func = dict()

        function_code = dict()
        code_pairs = inspect.getmembers(func_obj.__code__)
        for (key, value) in code_pairs:
            if str(key).startswith('co_'):
                if isinstance(value, bytes):
                    value = (list(value))
                function_code[key] = value
        func['code'] = function_code

        function_globals = dict()
        name = func['code']['co_name']
        function_globals[name] = name + '<function>'
        global_pairs = func_obj.__globals__.items()
        for (key, value) in global_pairs:
            if self.__is_default(value):
                function_globals[key] = value
        func['globals'] = function_globals

        return func

    def dictionary_function(self, dict_func):
        function_globals = dict_func['globals']
        function_globals['__builtins__'] = builtins
        code_args = dict_func['code']

        function_code = CodeType(code_args['co_argcount'],
                                 code_args['co_posonlyargcount'],
                                 code_args['co_kwonlyargcount'],
                                 code_args['co_nlocals'],
                                 code_args['co_stacksize'],
                                 code_args['co_flags'],
                                 bytes(code_args['co_code']),
                                 tuple(code_args['co_consts']),
                                 tuple(code_args['co_names']),
                                 tuple(code_args['co_varnames']),
                                 code_args['co_filename'],
                                 code_args['co_name'],
                                 code_args['co_firstlineno'],
                                 bytes(code_args['co_lnotab']),
                                 tuple(code_args['co_freevars']),
                                 tuple(code_args['co_cellvars']))

        temp = FunctionType(function_code, function_globals, code_args['co_name'])
        name = code_args['co_name']
        function_globals[name] = temp
        return FunctionType(function_code, function_globals, name)
