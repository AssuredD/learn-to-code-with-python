import unittest


def multiply(a, b):
    return a * b


class MultiplyTestCaste(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)


if __name__ == "__main__":
    unittest.main()
