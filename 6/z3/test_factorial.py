import sys
import unittest

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result


class TestFactorial(unittest.TestCase):
    
    def test_zero_and_one(self):
        """Проверка граничных случаев: 0 и 1"""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
    
    def test_simple_values(self):
        """Проверка маленьких чисел"""
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
    
    def test_bigger_values(self):
        """Проверка больших чисел"""
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(8), 40320)
        self.assertEqual(factorial(10), 3628800)
    
    def test_negative(self):
        """Отрицательные числа должны выдать ошибку"""
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-100)
    
    def test_overflow(self):
        """Проверка переполнения"""
        with self.assertRaises(ValueError):
            factorial(1000)
    
    def test_wrong_type(self):
        """Проверка передача не целых чисел """
        with self.assertRaises(TypeError):
            factorial(3.14)
        with self.assertRaises(TypeError):
            factorial("шесть")
        with self.assertRaises(TypeError):
            factorial([1, 2, 3])


if __name__ == "__main__":
    unittest.main(verbosity=2)