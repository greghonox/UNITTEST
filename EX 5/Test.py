from unittest.mock import Mock, patch
from unittest import TestCase, main

from main import *

class Tests(TestCase):
    def test_patching_class(self):
        with patch('main.Ajuda', autospec=True) as MockHelper:
            MockHelper.return_value.get_path.return_value = 'testing'
            worker = Worker()
            MockHelper.assert_called_once_with('db')
            self.assertEqual(worker.work(), 'testing')

main()