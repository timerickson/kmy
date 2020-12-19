import unittest
from kmy.kmy import Kmy

file_name = 'Test.kmy'


class TestTag(unittest.TestCase):
    def setUp(self):
        mm = Kmy.from_kmy_file(file_name)
        self.tags = mm.tags
        self.tag0 = self.tags[0]

    def test_read_tags_count(self):
        self.assertEqual(1, len(self.tags))

    def test_read_closed(self):
        self.assertEqual(False, self.tag0.closed)

    def test_read_tagcolor(self):
        self.assertEqual('#000000', self.tag0.tagColor)

    def test_read_name(self):
        self.assertEqual('Bar Tag', self.tag0.name)

    def test_read_id(self):
        self.assertEqual('G000001', self.tag0.id)


if __name__ == '__main__':
    unittest.main()
