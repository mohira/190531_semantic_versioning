import unittest


class SemVer:
    def __init__(self, major: int, minor: int, patch: int):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"


class TestSemVer(unittest.TestCase):
    def test_バージョンオブジェクトの文字列表現を取得できる(self):
        with self.subTest("1.4.2"):
            self.assertEqual("1.4.2", str(SemVer(1, 4, 2)))

        with self.subTest("1.5.8"):
            self.assertEqual("1.5.8", str(SemVer(1, 5, 8)))


if __name__ == "__main__":
    unittest.main()
