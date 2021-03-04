# TESTANDO O BASICO DE UMA CLASSE UNITTEST

from unittest import TestCase, main, skip
from unittest.result import failfast

class Basic(TestCase):
    
    ' A SEQUENCIA DE EXECUCAO ESTA ABAIXO '
    def setUp(self) -> None:
        ' A IDEIA AQUI É CHAMAR COMPONENTES QUE PODEM SER USADO NOS OUTROS TESTES '
        self.failfast = False
        print('INICIO ANTES DE CADA TESTES')

    @classmethod
    def setUpClass(cls) -> None:
        print('EXECUTO ANTES DOS TESTES DA CLASSE')
            
    def test_with_tips_asserts_1(self):
        self.assertEqual(10, 10) # a == b
        
    def test_with_tips_asserts_2(self):
        self.assertNotEqual(10, 20) # a != b
    
    def test_with_tips_asserts_3(self):
        self.assertTrue(True) # bool(x) is True
    
    def test_with_tips_asserts_4(self):
        self.assertFalse(False) # bool(x) is False
    
    # @skip('VAI DAR ERRO MESMO')
    def test_with_tips_asserts_5(self):
        self.assertIs(10, 20) # a is b
    
    def test_with_tips_asserts_6(self):
        self.assertIsNot(20, '10') # a not is b
    
    def test_with_tips_asserts_7(self):
        self.assertIsNone(None) # x is None
    
    def test_with_tips_asserts_8(self):
        self.assertIsNotNone(1) # x is not None
    
    def test_with_tips_asserts_9(self):
        self.assertIn(1, [1, 2]) # a in b
    
    def test_with_tips_asserts_10(self):
        self.assertNotIn(1, [2, 3, 4]) # a not in b
    
    def test_with_tips_asserts_11(self):
        self.assertIsInstance(True, bool) # a isistance b
    
    def test_with_tips_asserts_12(self):
        self.assertNotIsInstance('a', bool) # a isistance not b
        
    def test_with_tips_asserts_13(self):
        self.assertGreater(30, 20) # 10 > 20
        
    def test_with_tips_asserts_14(self):
        self.assertLess(9, 10) # 20 < 10

    def tearDown(self) -> None:
        print('FACO A LIMPEZA DE CADA TESTE')
        
    @classmethod
    def tearDownClass(cls):
        print('EXECUTO DEPOIS DE TODOS OS TESTES')        

main()