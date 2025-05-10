# Import needed modules
import unittest
from translator import translator


# Class for testing work
class TestTranslator(unittest.TestCase):
    def test_to_morse(self):
        self.assertEqual(translator("Hello world!!", "1"),
                         ".... . ._.. ._.. ___     .__ ___ ._. ._.. _.. _._.__ _._.__")
        self.assertEqual(translator("HElLo wOrld#", "1"),
                         ".... . ._.. ._.. ___     .__ ___ ._. ._.. _..")

    def test_to_alphanumeric(self):
        self.assertEqual(translator("'.... . ._.. ._.. ___     .__ ___ ._. ._.. _.. #", "2"),
                         "HELLO WORLD")
        self.assertEqual(translator("'.... . ._..3 ._.. ___", "2"),
                         "HELLO")


if __name__ == "__main__":
    unittest.main()
