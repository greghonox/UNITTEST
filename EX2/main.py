from unittest import main, TestCase
from unittest.mock import Mock
from os.path import isfile
from requests import get

class TestCoisas(TestCase):
    def test_existe_arquivo(self):
        self.assertTrue(self.verificar_arquivos(('/tmp/giphy.gif')))

    def test_nao_existe_arquivo(self):
        self.verificar_arquivos = Mock(return_value=False)
        self.assertFalse(self.verificar_arquivos(('/tmp/giphy.gif')))

    def test_pegar_google(self):
        self.assertEqual(self.pegar_google(), 200)

    def verificar_arquivos(self, arquivo): return isfile(arquivo)

    def pegar_google(self): return get('https://google.com.br').status_code

main()
