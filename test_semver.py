from __future__ import annotations

import unittest


class SemVer:
    def __init__(self, major: int, minor: int, patch: int):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"

    def __eq__(self, other: SemVer):
        return isinstance(other, SemVer) \
               and (self.major == other.major) \
               and (self.minor == other.minor) \
               and (self.patch == other.patch)


class TestSemVer(unittest.TestCase):
    def test_バージョンオブジェクトの文字列表現を取得できる(self):
        with self.subTest("1.4.2"):
            self.assertEqual("1.4.2", str(SemVer(1, 4, 2)))

        with self.subTest("1.5.8"):
            self.assertEqual("1.5.8", str(SemVer(1, 5, 8)))

    def test_等価性を比較できる(self):
        with self.subTest("1.4.2 と 1.4.2 は等しい"):
            self.assertEqual(SemVer(1, 4, 2), SemVer(1, 4, 2))

        with self.subTest("1.4.2 と 2.1.0 は等しくない "):
            self.assertNotEqual(SemVer(1, 4, 2), SemVer(2, 1, 0))


if __name__ == "__main__":
    unittest.main()
