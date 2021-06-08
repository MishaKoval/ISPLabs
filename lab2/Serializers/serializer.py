import inspect
import types


sort_keys = False
f_found = {}


def dump(obj, fp, indent=None, sort=False):
    string = dumps(obj, indent, sort)
    try:
        with open(fp, "w") as file:
            file.write(string)
    except FileNotFoundError:
        raise FileNotFoundError("File doesn't exist!")


def dumps(obj, indent=None, sort=False):
    global sort_keys
    sort_keys = sort
    if isinstance(indent, int) and indent > 0:
        space = " " * indent
        result_encode = inter_dumps(obj, space)
        if indent < 1:
            result_encode = result_encode.replace("\n", "")
    else:
        result_encode = inter_dumps(obj).replace("\n", "")
    return result_encode


def inter_dumps(obj, space="", new_space=""):
    global f_found
    if obj is None:
        return "null"
    elif obj is True:
        return "true"
    elif obj is False:
        return "false"
    elif obj is float("Inf"):
        return "Infinity"
    elif obj is float("-Inf"):
        return "-Infinity"
    elif obj is float("NaN"):
        return "NaN"
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif isinstance(obj, str):
        return '"' + obj.replace('\\', '\\\\').replace('"', '\\"') + '"'
    elif isinstance(obj, tuple):
        return dumps_dict(tuple_to_dict(obj), space, new_space)
    elif isinstance(obj, list):
        return dumps_list(obj, space, new_space)
    elif isinstance(obj, dict):
        return dumps_dict(obj, space, new_space)
    elif inspect.isclass(obj):
        return dumps_dict(class_to_dict(obj), space, new_space)
    elif inspect.ismodule(obj):
        return dumps_dict(module_to_dict(obj), space, new_space)
    elif inspect.isfunction(obj):
        result = dumps_dict(function_to_dict(obj), space, new_space)
        f_found = {}
        return result
    elif isinstance(obj, staticmethod):
        result = dumps_dict(static_method_to_dict(obj), step, new_step)
        f_found = {}
        return result
    elif isinstance(obj, classmethod):
        result = dumps_dict(class_method_to_dict(obj), step, new_step)
        f_found = {}
        return result
    elif my_isinstance(obj):
        return dumps_dict(object_to_dict(obj), space, new_space)
    elif isinstance(obj, bytes):
        return '"' + str(list(bytearray(obj))) + '"'
    elif isinstance(obj, types.CodeType):
        return dumps_dict(code_to_dict(obj), space, new_space)
    else:
        raise TypeError()


def dumps_dict(obj, space="", new_space=""):
    if not len(obj):
        return "{}"
    if sort_keys:
        obj = dict(sorted(obj.items()))
    new_space = "\n" + new_space
    result = "{" + new_space
    keys = list(obj)
    for i in keys[:-1]:
        result += (space
                   + '"'
                   + str(i)
                   + '"'
                   + ": "
                   + inter_dumps(obj[i],
                                 space,
                                 new_space.replace("\n", "")
                                 + space)
                   + "," + new_space)
    result += (space
               + '"'
               + str(keys[-1])
               + '"'
               + ": "
               + inter_dumps(obj[keys[-1]],
                             space,
                             new_space.replace("\n", "")
                             + space)
               + new_space
               + "}")
    return result


def dumps_list(obj, space="", new_space=""):
    if not len(obj):
        return "[]"
    new_space = "\n" + new_space
    result = "[" + new_space
    for i in range(len(obj) - 1):
        result += (space
                   + inter_dumps(obj[i],
                                 space,
                                 new_space.replace("\n", "")
                                 + space)
                   + ","
                   + new_space)
    result += (space
               + inter_dumps(obj[-1],
                             space,
                             new_space.replace("\n", "")
                             + space)
               + new_space
               + "]")
    return result


def my_isinstance(obj):
    if not hasattr(obj, "__dict__"):
        return False
    if inspect.isroutine(obj):
        return False
    if inspect.isclass(obj):
        return False
    else:
        return True


def tuple_to_dict(obj):
    return {"tuple_type": list(obj)}


def code_to_dict(obj_code):
    return {
        "code_type": {
            "co_argcount": obj_code.co_argcount,
            "co_posonlyargcount": obj_code.co_posonlyargcount,
            "co_kwonlyargcount": obj_code.co_kwonlyargcount,
            "co_nlocals": obj_code.co_nlocals,
            "co_stacksize": obj_code.co_stacksize,
            "co_flags": obj_code.co_flags,
            "co_code": obj_code.co_code,
            "co_consts": obj_code.co_consts,
            "co_names": obj_code.co_names,
            "co_varnames": obj_code.co_varnames,
            "co_filename": obj_code.co_filename,
            "co_name": obj_code.co_name,
            "co_firstlineno": obj_code.co_firstlineno,
            "co_lnotab": obj_code.co_lnotab,
            "co_freevars": obj_code.co_freevars,
            "co_cellvars": obj_code.co_cellvars,
        }
    }


def module_to_dict(obj):
    return {"module_type": obj.__name__}


def object_to_dict(obj):
    return {
        "instance_type": {
            "class": class_to_dict(obj.__class__),
            "vars": obj.__dict__,
        }
    }


def function_to_dict(obj):
    obj_code = obj.__code__
    analysis = object_analysis(obj, obj_code)
    return {
        "function_type": {
            "__globals__": analysis,
            "__name__": obj.__name__,
            "__code__": code_to_dict(obj_code),
            "__defaults__": obj.__defaults__,
            "__closure__": obj.__closure__
        }
    }


def object_analysis(obj, obj_code):
    global f_found
    f_found[obj] = True
    analysis = {}
    for i in obj_code.co_names:
        try:
            if inspect.isclass(obj.__globals__[i]):
                analysis[i] = class_to_dict(obj.__globals__[i])
            elif inspect.isfunction(obj.__globals__[i]):
                if obj.__globals__[i] not in f_found:
                    analysis[i] = function_to_dict(obj.__globals__[i])
            elif isinstance(obj.__globals__[i], staticmethod):
                if obj.__globals__[i].__func__ not in analysis:
                    analysis[i] = static_method_to_dict(obj.__globals__[i])
            elif isinstance(obj.__globals__[i], classmethod):
                if obj.__globals__[i].__func__ not in analysis:
                    analysis[i] = class_method_to_dict(obj.__globals__[i])
            elif inspect.ismodule(obj.__globals__[i]):
                analysis[i] = module_to_dict(obj.__globals__[i])
            elif my_isinstance(obj.__globals__[i]):
                analysis[i] = object_to_dict(obj.__globals__[i])
            elif isinstance(
                    obj.__globals__[i],
                    (dict, list, int, float, bool, type(None), tuple, str),
            ):
                analysis[i] = obj.__globals__[i]
        except KeyError:
            pass
    for i in obj_code.co_consts:
        if isinstance(i, types.CodeType):
            analysis.update(object_analysis(obj, i))
    return analysis


def static_method_to_dict(obj):
    return {"static_method_type": function_to_dict(obj.__func__)}


def class_to_dict(obj):
    dpns = ()
    if len(obj.__bases__) != 0:
        for i in obj.__bases__:
            if i.__name__ != "object":
                dpns += (class_to_dict(i),)
    args = {}
    st_args = dict(obj.__dict__)
    if len(st_args) != 0:
        for i in st_args:
            if inspect.isclass(st_args[i]):
                args[i] = class_to_dict(st_args[i])
            elif inspect.isfunction(st_args[i]):
                if st_args[i] not in f_found:
                    args[i] = function_to_dict(st_args[i])
            elif isinstance(st_args[i], staticmethod):
                if st_args[i].__func__ not in f_found:
                    args[i] = static_method_to_dict(st_args[i])
            elif isinstance(st_args[i], classmethod):
                if st_args[i].__func__ not in f_found:
                    args[i] = class_method_to_dict(st_args[i])
            elif inspect.ismodule(st_args[i]):
                args[i] = module_to_dict(st_args[i])
            elif my_isinstance(st_args[i]):
                args[i] = object_to_dict(st_args[i])
            elif isinstance(
                    st_args[i],
                    (
                            dict,
                            list,
                            int,
                            float,
                            bool,
                            type(None),
                            tuple,
                    ),
            ):
                args[i] = st_args[i]
    return {"class_type": {"name": obj.__name__, "bases": dpns, "dict": args}}


def class_method_to_dict(obj):
    return {"class_method_type": function_to_dict(obj.__func__)}


def load(fp):
    try:
        with open(fp, "r") as file:
            data = file.read()
    except FileNotFoundError:
        raise FileNotFoundError("file doesn't exist")
    return loads(data)


def loads(data):
    index = 0
    try:
        while data[index] == " " or data[index] == "\n":
            index += 1
    except IndexError:
        pass
    obj, index = load_symbols(data, index)

    try:
        while True:
            if data[index] != " " and data[index] != "\n":
                raise StopIteration(index)
            index += 1
    except IndexError:
        pass
    return obj


def load_symbols(data, index):
    if data[index] == '"':
        obj, index = load_string(data, index + 1)
    elif data[index].isdigit() or (data[index] == "-" and data[index + 1].isdigit()):
        obj, index = load_digit(data, index)
    elif data[index] == "{":
        obj, index = load_dict(data, index + 1)
    elif data[index] == "[":
        obj, index = load_list(data, index + 1)
    elif data[index] == "n" and data[index: index + 4] == "null":
        obj = None
        index += 4
    elif data[index] == "t" and data[index: index + 4] == "true":
        obj = True
        index += 4
    elif data[index] == "f" and data[index: index + 5] == "false":
        obj = False
        index += 5
    elif data[index] == "N" and data[index: index + 3] == "NaN":
        obj = False
        index += 3
    elif data[index] == "I" and data[index: index + 8] == "Infinity":
        obj = float("Infinity")
        index += 8
    elif data[index] == "-" and data[index: index + 9] == "-Infinity":
        obj = float("-Infinity")
        index += 9
    else:
        raise StopIteration(index)
    return obj, index


def load_string(data, index):
    first = index
    opened = False
    try:
        while data[index] != '"' or opened:
            if data[index] == "\\":
                opened = not opened
            else:
                opened = False
            index += 1
    except IndexError:
        raise StopIteration(index)
    return data[first:index], index + 1


def load_digit(data, index):
    first = index
    try:
        while (
                data[index] == "."
                or data[index].isdigit()
                or data[index] == "e"
                or data[index] == "E"
                or data[index] == "-"
                or data[index] == "+"
        ):
            index += 1
    except IndexError:
        pass
    res = data[first:index]
    try:
        return int(res), index
    except ValueError:
        try:
            return float(res), index
        except ValueError:
            raise StopIteration(index)


def load_dict(data, index):
    args = {}
    comma = False
    colon = False
    phase = False
    temp = None

    try:
        next_char = data[index]
    except IndexError:
        raise StopIteration(index)
    while True:
        if next_char == "}":
            break
        elif next_char == " " or next_char == "\n":
            index += 1
        elif next_char == ",":
            if comma is False:
                raise StopIteration(index)
            index += 1
            phase = False
            comma = False
        elif next_char == ":":
            if colon is False:
                raise StopIteration(index)
            index += 1
            phase = True
            colon = False
        elif not comma and not phase:
            if next_char == '"':
                obj, index = load_string(data, index + 1)
                if obj in args:
                    raise StopIteration(index)
                temp = obj
                phase = False
                colon = True
            else:
                raise StopIteration(index)
        elif not colon and phase:
            obj, index = load_symbols(data, index)
            args[temp] = obj

            comma = True
        else:
            raise StopIteration(index)
        try:
            next_char = data[index]
        except IndexError:
            raise StopIteration(index)
    if not comma and not colon and len(args) != 0:
        raise StopIteration(index)
    if "function_type" in args and len(args.keys()) == 1:
        return dict_to_func(args["function_type"]), index + 1
    if "static_method_type" in args and len(args.keys()) == 1:
        return staticmethod(args["static_method_type"]), index + 1
    if "class_method_type" in args and len(args.keys()) == 1:
        return classmethod(args["class_method_type"]), index + 1
    if "class_type" in args and len(args.keys()) == 1:
        return dict_to_class(args["class_type"]), index + 1
    if "instance_type" in args and len(args.keys()) == 1:
        return dict_to_obj(args["instance_type"]), index + 1
    if "module_type" in args and len(args.keys()) == 1:
        return dict_to_module(args["module_type"]), index + 1
    if "code_type" in args and len(args.keys()) == 1:
        return dict_to_code(args["code_type"]), index + 1
    if "tuple_type" in args and len(args.keys()) == 1:
        return tuple(args["tuple_type"]), index + 1
    else:
        if sort_keys:
            return dict(sorted(args.items())), index + 1
        else:
            return args, index + 1


def dict_to_func(obj):
    closure = None
    if obj["__closure__"] is not None:
        closure = obj["__closure__"]
    res = types.FunctionType(
        globals=obj["__globals__"],
        code=obj["__code__"],
        name=obj["__name__"],
        closure=closure,
    )
    try:
        setattr(res, "__defaults__", obj["__defaults__"])
    except TypeError:
        pass
    funcs = collect_funcs(res, {})
    funcs.update({res.__name__: res})
    set_funcs(res, {res.__name__: True}, funcs)
    res.__globals__.update(funcs)
    res.__globals__["__builtins__"] = __import__("builtins")
    return res


def collect_funcs(obj, is_visited):
    for i in obj.__globals__:
        attr = obj.__globals__[i]
        if inspect.isfunction(attr) and attr.__name__ not in is_visited:
            is_visited[attr.__name__] = attr
            is_visited = collect_funcs(attr, is_visited)
    return is_visited


def set_funcs(obj, is_visited, analyse):
    for i in obj.__globals__:
        attr = obj.__globals__[i]
        if inspect.isfunction(attr) and attr.__name__ not in is_visited:
            is_visited[attr.__name__] = True
            attr.__globals__.update(analyse)
            is_visited = set_funcs(attr, is_visited, analyse)
    return is_visited


def dict_to_class(obj):
    try:
        return type(obj["name"], obj["bases"], obj["dict"])
    except IndexError:
        raise StopIteration("Incorrect class!")


def dict_to_obj(obj):
    try:

        def __init__(self):
            pass

        cls = obj["class"]
        temp = cls.__init__
        cls.__init__ = __init__
        res = obj["class"]()
        res.__dict__ = obj["vars"]
        res.__init__ = temp
        res.__class__.__init__ = temp
        return res
    except IndexError:
        raise StopIteration("Incorrect object!")


def dict_to_module(obj):
    try:
        return __import__(obj)
    except ModuleNotFoundError:
        raise ImportError(str(obj) + " not found!")


def dict_to_code(obj):
    return types.CodeType(
        obj["co_argcount"],
        obj["co_posonlyargcount"],
        obj["co_kwonlyargcount"],
        obj["co_nlocals"],
        obj["co_stacksize"],
        obj["co_flags"],
        bytes(bytearray(load_list(obj["co_code"], 1)[0])),
        obj["co_consts"],
        obj["co_names"],
        obj["co_varnames"],
        obj["co_filename"],
        obj["co_name"],
        obj["co_firstlineno"],
        bytes(bytearray(load_list(obj["co_lnotab"], 1)[0])),
        obj["co_freevars"],
        obj["co_cellvars"],
    )


def load_list(data, index):
    args = []
    comma = False

    try:
        next_char = data[index]
    except IndexError:
        raise StopIteration(index)
    while True:
        if next_char == "]":
            break
        elif next_char == " " or next_char == "\n":
            index += 1
        elif next_char == ",":
            if comma is False:
                raise StopIteration(index)
            index += 1
            comma = False
        elif not comma:
            obj, index = load_symbols(data, index)
            args.append(obj)

            comma = True
        else:
            raise StopIteration(index)
        try:
            next_char = data[index]
        except IndexError:
            raise StopIteration(index)
    if not comma and len(args) != 0:
        raise StopIteration(index)
    return list(args), index + 1
