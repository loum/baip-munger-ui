import unittest2

from baip_munger_ui.utils import allowed_file


class TestUtils(unittest2.TestCase):
    def test_allowed_files(self):
        """Allowed filename extensions.
        """
        # Given a filename.
        filename = 'banana.html'

        # and a list of acceptable extensions
        extensions = ['html', 'htm']

        # when I check for acceptable extensions
        received = allowed_file(filename, extensions)

        # then I should receive True
        msg = 'Filename extension check should return True'
        self.assertTrue(received, msg)

    def test_not_allowed_files(self):
        """Allowed filename extensions: not in extension list.
        """
        # Given a filename.
        filename = 'banana.html'

        # and a list of acceptable extensions that does not feature
        # the extension of the given filename
        extensions = ['htm']

        # when I check for acceptable extensions
        received = allowed_file(filename, extensions)

        # then I should receive False
        msg = 'Missing filename extension check should return False'
        self.assertFalse(received, msg)

    def test_allowed_files_no_extension(self):
        """Allowed filename extensions: not in extension list.
        """
        # Given a filename with no extension.
        filename = 'banana'

        # and a list of acceptable extensions that does not feature
        # the extension of the given filename
        extensions = ['html', 'htm']

        # when I check for acceptable extensions
        received = allowed_file(filename, extensions)

        # then I should receive False
        msg = 'Filename extension check should return False'
        self.assertFalse(received, msg)
