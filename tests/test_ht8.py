from unittest import TestCase
import ht_8_task_2


class TestHomeWork8Task2(TestCase):
    def setUp(self):
        self.cell1 = ht_8_task_2.Cell(30)
        self.cell2 = ht_8_task_2.Cell(25)
        self.cell3 = ht_8_task_2.Cell(10)
        self.cell4 = ht_8_task_2.Cell(15)

    def test1(self):
        self.assertIsNot(self.cell1, self.cell2)
        self.assertIsNot(self.cell3, self.cell4)

    def test2(self):
        self.assertIsNotNone(self.cell1)
        self.assertIsNotNone(self.cell2)
        self.assertIsNotNone(self.cell3)
        self.assertIsNotNone(self.cell4)

    def test3(self):
        self.assertEqual(self.cell1 + self.cell2, 55)
        self.assertNotEqual(self.cell1 + self.cell2, 10)
        self.assertTrue(self.cell1 + self.cell2)

    def test4(self):
        self.assertEqual(self.cell2 - self.cell1,
                         "Разность отрицательна, "
                         "поэтому операция не выполняется")
        self.assertNotEqual(self.cell1 - self.cell2, 11)
        self.assertTrue(self.cell1 - self.cell2)

    def test5(self):
        self.assertEqual(self.cell1 * self.cell2, 750)
        self.assertNotEqual(self.cell1 * self.cell2, 800)
        self.assertIsNotNone(self.cell1 * self.cell2)

    def test6(self):
        self.assertEqual(self.cell4 / self.cell3, 1)
        self.assertNotEqual(self.cell4 / self.cell3, 2)
        self.assertIsNotNone(self.cell4 / self.cell3)
