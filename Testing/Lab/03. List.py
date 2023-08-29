class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)

import unittest

class IntegerListTests(unittest.TestCase):
    def SetUp(self):
        self.integer_list = IntegerList(1, 2, 3, 5.5)

    def test_initializing(self):
        expected = [1, 2, 3]
        self.integer_list.get_data()
        self.assertEqual(expected, self.integer_list.get_data())

    def test_add_operation_list_change(self):
        expected = self.integer_list.get_data() + [5]
        self.integer_list.add(5)
        self.assertEqual(expected, self.integer_list.get_data())

    def test_add_operation_error(self):
        with self.assertRaises(Exception) as ex:
            self.integer_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index(self):
        expected = 2
        self.integer_list.remove_index()
