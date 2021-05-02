class Objects:
    def __init__(self):
        self.number = 9999
        self.string = "MiKo"
        self.list = ["Kovalevskiy", 1.44, 666]
        self.dict = {"1": 1, "2": "1"}


class Test:
    def __init__(self):
        self.str = 'TEST'
        self.number = 5


test_obj = Test()

global_obj = 'GLOBAL'


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def function():
    return global_obj + 'ELITE'
