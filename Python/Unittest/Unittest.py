Unittest
Структура

import unittest
from main import my_function

Tests…

if __name__ == '__main__':
    main()


Проверка на заготовленные задачи

class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

Проверка на тип возвращяющего значения

class Test_valid_walk(unittest.TestCase):
    """Тест на тип возвращяющего значения:
     str, int, float, bool, tuple , и None"""
    def test_valid_walk(self):
        self.assertEqual(type(is_valid_walk(arr1)), bool)

------------------------------------------------------------------------------------------------------------------------------------

Создание шаблонна тестов проекта (Переименуй название)

Edit configuration ->  + ->   Python tests ->   Unittests ->  Custom ->
discover -s tests -p '*_test.py'
Что обозначает  “Найди тесты в папке tests под названием ххх_test”




