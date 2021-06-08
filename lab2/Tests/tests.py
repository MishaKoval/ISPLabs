t1 = [[[[[[[[[[[3, [[[[[[[[[[[[[[[[[[[[[[[[[[[55.3, [[[[[[[[[[4]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

t2 = [(3, 4), 5]

t3 = (8, 6)

objects = [tuple(), []]

string = "4 43    43"


def simple_func():
    pass


def simple_recursion():
    return simple_recursion()


def double_func_recursion_1():
    return double_func_recursion_2()


def double_func_recursion_2():
    return double_func_recursion_1()


gl1 = 53


def func_with_globals_and_builtins():
    print(simple_func)
    return gl1


def func_in_func(a, f, l):
    print(a)

    def first(b):
        print(a + b)

        def second(c):
            print(a + b + c)

        second(l)

    first(f)


def func_with_defaults(a=1, b=3):
    return a + b


def tuple_returner(a, b, c, d):
    x = a + b
    y = c + d
    return (x, y)


def set_returner(a, b, c, d):
    x = a + b
    y = c + d
    return {x, y}


def func_with_args_sum(*args):
    return sum(args)


def func_with_args_d(**args):
    return args


def counter(func):
    count = 0

    def wrapper(*args):
        func(*args)
        nonlocal count
        count += 1
        print(count)

    return wrapper


@counter
def check_decorator():
    pass


def p(a=simple_func):
    return a


simplelambda = lambda x: x * x

lambda_in_lambda = lambda x: simplelambda(x) * x


def lambda_in_function(a=2):
    print(lambda_in_lambda(a))


class Empty_cls:
    pass


class Simple_cls:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + " : " + str(self.y)


class Cls_with_inheritance(Empty_cls):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Cls_with_staticmethod:
    @staticmethod
    def print_hello():
        print("hello")


class Cls_with_classmethod:
    @classmethod
    def print_cls(cls):
        print(cls)


class Inherited_cls(Cls_with_classmethod, Cls_with_staticmethod):
    pass


class B:
    a = 666
    b = [333, 666, 'www']

    @staticmethod
    def c(n):
        return str(n) + '!!!'

    @staticmethod
    def b_func():
        return 'Hello from B class method'