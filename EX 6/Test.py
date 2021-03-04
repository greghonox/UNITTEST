from unittest import TestCase, mock

from main import *


class Tests(TestCase):
    def test_returns_true_if_url_found(self):
        with mock.patch('requests.get') as mock_request:
            url = 'http://google.com'
            mock_request.return_value.status_code = 200
            self.assertTrue(url_exists(url))

    def test_returns_false_if_url_not_found(self):
        with mock.patch('requests.get') as mock_request:
            url = 'http://google.com/nonexistingurl'
            mock_request.return_value.status_code = 404
            self.assertFalse(url_exists(url))

    @mock.patch('requests.get')
    def test_returns_false_mock(self, mocks):
        mocks.return_value.status_code = 200
        url = 'http://google.com/nonexistingurl'
        self.assertTrue(url_exists(url))

    def test_return_text_content(self):
        with mock.patch('requests.get') as mocks:
            url = 'http://google.com.br'
            respostas_esperada = b'JESUS VAI VOLTAR EM BREVE'
            mocks.return_value.content = respostas_esperada
            self.assertEqual(process_response(url), respostas_esperada + b'1')

    @mock.patch('requests.get')
    def test_return_text_content_decorate(self, mocks):
        url = 'http://google.com.br'
        respostas_esperada = b'JESUS VAI VOLTAR EM BREVE'
        mocks.return_value.content = respostas_esperada
        self.assertEqual(process_response(url), respostas_esperada + b'1')

    @mock.patch('requests.get', return_value=True)
    def test_returns_false_mock2(self, mocks):
        ' NAO SEI PORQUE ELE NAO ENTENDE '
        mocks.return_value.status_code = 200
        url = 'http://google.com/nonexistingurl'
        self.assertTrue(mocks(url))

    @mock.patch('main.open')
    @mock.patch('main.requests.get', autospec=True)
    def test_download(self, mock_get, mock_open):
        url = 'https://example.com/sample.txt'
        mock_open('/tmp/test.tt')
        download(url)

class FakeResponse(object):
    # default response attributes
    status_code = 200
    content = "Some content"

class ProcessResponseTests(TestCase):
    def test_response_content_is_not_empty(self):
        with mock.patch('requests.get') as mock_request:
            url = 'http://google.com'
            fake_response = FakeResponse()
            mock_request.return_value = fake_response
            fake_response.status_code = 404
            fake_response.content = "Hello, world"
            self.assertIsNotNone(fake_response.content)

