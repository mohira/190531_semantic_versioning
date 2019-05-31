import unittest


def add(num1: int, num2: int):
    return num1 + num2  # 仮実装


class MyTestCase(unittest.TestCase):
    def test_2つの整数の和を計算できる(self):
        self.assertEqual(7, add(3, 4))


if __name__ == "__main__":
    unittest.main()
