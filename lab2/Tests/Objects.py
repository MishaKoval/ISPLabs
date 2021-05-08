class Objects:
    def __init__(self):
        self.number = 9999
        self.string = "MiKo"
        self.list = [1.2, 'Allo', 465, {'a': 5}]
        self.dict = {"1": 1, "2": "1"}


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


class Test:
    def __init__(self):
        self.str = "TEST"
        self.number = 5


test_obj = Test()

global_obj = "GLOBAL"


def function():
    return global_obj + "ELITE"
