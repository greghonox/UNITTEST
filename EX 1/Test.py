from unittest import TestCase, mock, main
from main import *

resposta_esperada = {'name': 'Georgia', 'gender': 'female', 'probability': 0.98, 'count': 6130}

class Test(TestCase):
    def _mock_response(self, status=200, content="CONTENT", json_data=None, raise_for_status=None):
        mock_resp = mock.Mock()
        mock_resp.raise_for_status = mock.Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        mock_resp.status_code = status
        mock_resp.content = content
        if json_data:
            mock_resp.json = mock.Mock(
                return_value=json_data
            )
        return mock_resp

    def test_sexo_feminino(self):
        self.assertEqual(pegar_sexo('Geogia Maria').json(), resposta_esperada)

    @mock.patch('main.get', return_value=resposta_esperada)
    def test_sexo_feminino_mock(self, mocks):
        mockk = self._mock_response()
        mocks.return_value = mockk
        self.assertEqual(mocks('Geogia Maria').json(), resposta_esperada)


main()