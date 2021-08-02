import unittest

from functions import check_positiveness


class TestJar(unittest.TestCase):

    def test_check_positiveness(self):
        self.assertEqual(
            check_positiveness(1, "int"),
            True
        )
        self.assertEqual(
            check_positiveness(0, "int"),
            True
        )
        self.assertEqual(
            check_positiveness(-1, "int"),
            False
        )
        self.assertEqual(
            check_positiveness("aaa", "int"),
            False
        )


if __name__ == '__main__':
    unittest.main()
