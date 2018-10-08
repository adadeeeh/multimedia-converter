import os
import unittest

from common import util


class TestUtil(unittest.TestCase):
    def test_filename_unique(self):
        filename1 = util.generate_filename()
        filename2 = util.generate_filename()
        self.assertNotEqual(filename1, filename2)

    def test_get_filename(self):
        filename = util.get_filename('test', 'ext')
        self.assertEqual(filename, 'test.ext')

    def test_get_temp_filename(self):
        filename = util.get_temp_filename('test')
        self.assertEqual(filename, 'test.tmp')

    def test_get_temp_path(self):
        path = util.get_temp_path('test')
        self.assertEqual(path, os.path.join(util.UPLOAD_FOLDER, 'test.tmp'))

    def test_output_path(self):
        path = util.get_output_path('test', 'ext')
        self.assertEqual(path, os.path.join(util.UPLOAD_FOLDER, 'test.ext'))


if __name__ == '__main__':
    unittest.main()
