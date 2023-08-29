from functools import reduce
from typing import List


class Calculator:

    @staticmethod
    def add(*args: List[int]):
        return sum(args)

    @staticmethod
    def multiply(*args: List[int]):
        return reduce(lambda a, b: a * b, args)

    @staticmethod
    def divide(*args: List[int]):
        return reduce(lambda a, b: a / b, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda a, b: a - b, args)




