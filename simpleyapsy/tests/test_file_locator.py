import os
import unittest
import tempfile
from simpleyapsy.file_locator import FileLocator


class TestClass:
    pass


class TestFileLocator(unittest.TestCase):
    def setUp(self):
        self.file_locator = FileLocator()

    def test_set_file_getters(self):
        current_file_getters = self.file_locator.file_getters[0]
        # Create a abstract object for testing
        obj = TestClass()
        self.file_locator.set_file_getters(obj)
        self.assertNotIn(current_file_getters, self.file_locator.file_getters)
        self.assertIn(obj, self.file_locator.file_getters)

    def test_add_file_getters(self):
        test_obj = TestClass()
        self.file_locator.add_file_getters(test_obj)
        self.assertIn(test_obj, self.file_locator.file_getters)

    def test_collect_filepaths(self):
        filename = 'test.py'
        with tempfile.TemporaryDirectory() as temp_dir:
            filepath = os.path.join(temp_dir, filename)
            open(filepath, 'a').close()
            filepaths = self.file_locator.collect_filepaths(temp_dir)
        self.assertIn(filepath, filepaths)

    def test_add_get_set_plugin_filepaths(self):
        filepath = 'my/test/filepath'
        self.file_locator.add_filepath(filepath)
        filepaths = self.file_locator.get_plugin_filepaths()
        self.assertIn(filepath, filepaths)
        set_filepath = 'new/set/filepath'
        self.file_locator.set_filepath(set_filepath)
        filepaths = self.file_locator.get_plugin_filepaths()
        self.assertIn(set_filepath, filepaths)
        self.assertNotIn(filepath, filepaths)


if __name__ == '__main__':
    unittest.main()
