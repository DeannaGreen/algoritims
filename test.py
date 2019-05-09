import unittest
from app import dupe2
from app import students
from app import my_reverse2
from app import my_shuffle2
from app import common
from app import sort01
from app import sum

class AlgorithmTestCase(unittest.TestCase):

    def test_dupe(self):
        result = dupe2([1, 2, 1])
        self.assertEqual(result, '[1]')

    def test_students(self):
        result = students()
        self.assertEqual(result, "[['john', 'bob'], ['john', 'madison'], ['bob', 'john'], ['bob', 'madison']]")

    def test_reverse(self):
        result = my_reverse2()
        self.assertEqual(result, "[4, 3, 2, 1]")

    def test_shuffle(self):
        result = my_shuffle2()
        self.assertNotEqual(result, "[1, 2, 3, 4]")

    def test_common(self):
        result = common()
        self.assertEqual(result, "{'the': 3, 'cat': 1, 'in': 1, 'bag': 1}")

    def test_sort01(self):
        result = sort01()
        self.assertEqual(result, "[0, 0, 0, 1, 1]")

    def test_sum(self):
        result = sum()
        self.assertEqual(result, "true")

if __name__ == '__main__':
    unittest.main()
