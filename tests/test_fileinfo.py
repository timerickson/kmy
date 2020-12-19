import unittest
from kmy.kmy import Kmy

file_name = 'Test.kmy'


class TestFileInfo(unittest.TestCase):
    def setUp(self):
        mm = Kmy.from_kmy_file(file_name)
        self.fileInfo = mm.fileInfo

    def test_read_creationDate(self):
        self.assertEqual('2020-12-13', self.fileInfo.creationDate)

    def test_read_lastModifiedDate(self):
        self.assertEqual('2020-12-13', self.fileInfo.lastModifiedDate)

    def test_read_version(self):
        self.assertEqual('1', self.fileInfo.version)

    def test_read_fixVersion(self):
        self.assertEqual('5', self.fileInfo.fixVersion)


if __name__ == '__main__':
    unittest.main()
