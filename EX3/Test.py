from main import *
from unittest import main, TestCase, mock

class Test(TestCase):
    @mock.patch('main.get', return_value={'nome': 'gregorio'})
    def test_conexao(self, mocks):
        self.assertIsInstance(mocks(), dict)

class TestOndeEstou(TestCase):
    @mock.patch('main.getcwd', return_value='/home/gregorio')
    def test_onde_estou(self, mocks):
        self.assertIsInstance(estouAqui(), str)

    @mock.patch('main.getcwd', return_value='/home/gregorio')
    def test_onde_estou_lugar(self, mocks):
        self.assertEqual(estouAqui(), '/home/gregorio')

    @mock.patch('main.cpu_count', return_value=10)
    @mock.patch('main.platform', return_value='Linux')
    def test_outras_coisa(self, *mocks):
        self.assertEqual(algumasCoisa(), (10, 'Linux'))

class TestWith(TestCase):
    def test_onde_estou(self):
        with mock.patch('main.cpu_count', return_value=10) as m1:
            with mock.patch('main.platform', return_value='Windows') as m2:
                self.assertEqual(m1(), 10)
                self.assertEqual(m2(), 'Linux')

if(__name__ == "__main__"): main()