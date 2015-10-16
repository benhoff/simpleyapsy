import os
import unittest
import tempfile
from pluginmanager.file_getters import WithInfoFileGetter


class TestWithInfoFileGetter(unittest.TestCase):
    def setUp(self):
        self.file_getter = WithInfoFileGetter()
        self._plugin_file_name = 'plugin.{}'

    def test_set_file_extension(self):
        test_extension = 'test'
        self.file_getter.set_file_extensions(test_extension)
        self.assertIn(test_extension, self.file_getter.extensions)

    def test_add_file_extensions(self):
        new_extension = 'test'
        previous_extension = self.file_getter.extensions[0]
        self.file_getter.add_file_extensions(new_extension)
        self.assertIn(new_extension, self.file_getter.extensions)
        self.assertIn(previous_extension, self.file_getter.extensions)

    def test_plugin_valid(self):
        valid_filepath = 'file.yapsy-plugin'
        unvalid_filepath = 'file.bad'
        valid_filepath = self.file_getter.plugin_valid(valid_filepath)
        unvalid_filepath = self.file_getter.plugin_valid(unvalid_filepath)
        self.assertTrue(valid_filepath)
        self.assertFalse(unvalid_filepath)

    def _create_tempfiles(self):
        with tempfile.TemporaryDirectory() as test_dir:
            file_template = os.path.join(test_dir,
                                         self._plugin_file_name)

            plugin_file = open(file_template.format('yapsy-plugin'), 'w+')
            fake_python = open(file_template.format('py'), 'w+')

            python_file_name = fake_python.name[:-3]
            yapsy_contents = """
            [Core]\n
            Name = Test\n
            Module = {}\n""".format(python_file_name)

            plugin_file.write(yapsy_contents)
            plugin_file.close()
            fake_python.close()
            info = self.file_getter.get_plugin_infos(test_dir)
            files = self.file_getter.get_plugin_filepaths(test_dir)
        return info, files

    def test_get_plugin_info(self):
        info, _ = self._create_tempfiles()
        self.assertNotEqual(info, [])

    def test_get_plugin_filepath(self):
        _, files = self._create_tempfiles()
        file_name = self._plugin_file_name.format('py')
        python_file = os.path.basename(files.pop())
        self.assertEqual(file_name, python_file)
