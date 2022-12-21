'''
Написать тесты для ДЗ уроков 1-8
1) не менее 10 тестов
2) желательно с разными ф-циями (assertEqual, assertRaises и т.д.)
3) тесты не должны быть вместе с исходным кодом
(нужно разместить в разных модулях)
'''

from unittest import TestCase
import ht_3_task_3
import ht_3_task_6
import ht_7_task_2


class MyTest(TestCase):
    def setUp(self):
        self.road1 = ht_7_task_2.Road(5000, 20)
        self.road2 = ht_7_task_2.Road(2500, 30)

    def test1_ht_3_task_3(self):
        self.assertEqual(ht_3_task_3.my_func(3, 4, 5), 9)
        self.assertEqual(ht_3_task_3.my_func(-1, 0, 10), 10)
        self.assertNotEqual(ht_3_task_3.my_func(-1, 0, 10), 13)

    def test2_ht_3_task_6(self):
        self.assertEqual(ht_3_task_6.int_func("abc"), "Abc")
        self.assertEqual(ht_3_task_6.int_func("тест"), "Тест")

    def test3_ht_7_task_2(self):
        self.assertEqual(self.road1.get_weight(), 12500.0)
        self.assertEqual(self.road2.get_weight(), 9375.0)
        self.assertNotEqual(self.road2.get_weight(), 0)

