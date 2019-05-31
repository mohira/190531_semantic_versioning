import unittest


class SemVer:
    def __init__(self, major: int, minor: int, patch: int):
        pass


class TestSemVer(unittest.TestCase):
    def test_バージョンオブジェクトを生成できる(self):
        SemVer(major=1, minor=4, patch=2)


if __name__ == "__main__":
    unittest.main()
