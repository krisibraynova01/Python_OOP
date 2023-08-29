import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "test_type", "sound_type")

    def test_is_initialized(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("test_type", self.mammal.type)
        self.assertEqual("sound_type", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_is_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("Test makes sound_type", result)

    def test_if_get_kingdom_returns_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_if_info_return(self):
        result = self.mammal.info()
        self.assertEqual("Test is of type test_type", result)

if __name__ == "__main__":
    unittest.main()
