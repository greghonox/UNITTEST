from unittest import main, mock, TestCase
from os import urandom

def simple_urandom(length): return 'f' * length

class TestRandom(TestCase):
    @mock.patch('__main__.urandom', side_effect=simple_urandom)
    def test_urandom(self, urandom_function):
        assert urandom(5) == 'fffff'

    @mock.patch('__main__.urandom', side_effect=simple_urandom)
    def test_urandom2(self, urandom_function):
        self.assertNotEqual(urandom(5), 'f'*5)

main()