import unittest
from main import ordenar_lista

class TestOrdenarLista(unittest.TestCase):

    def test_no_enteros(self):    
        result = ordenar_lista([41,68,52,4,63,"hola",74,51])
        self.assertEqual(result, "Todos los elementos deben ser enteros")
    
    def test_successful_result(self):
        result = ordenar_lista([6,52,7,58,2,40,69,85,0,48,41,45,87,963,55,48])
        self.assertEqual(isinstance(result, list), True)
        expected_result = [0, 2, 6, 7, 40, 41, 45, 48, 48, 52, 55, 58, 69, 85, 87, 963]
        self.assertSequenceEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()