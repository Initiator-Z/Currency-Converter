import unittest
from checks import check_arguments, check_date


class TestCheckArguments(unittest.TestCase):

    def test_checkarg(self):
        testarg1 = ['a', 'b', 'c']
        testarg2 = ['a', 'b', 'c', 'd']
        testarg3 = ['a']
        testarg4 = []

        self.assertEqual(check_arguments(testarg1), testarg1)
        with self.assertRaises(SystemExit):
            check_arguments(testarg2)
        with self.assertRaises(SystemExit):
            check_arguments(testarg3)
        with self.assertRaises(SystemExit):
            check_arguments(testarg4)

class TestCheckDate(unittest.TestCase):

    def test_checkdate(self):
        date1 = '2020-01-01'
        date2 = '2020/01/01'
        date3 = '2020-13-01'
        date4 = '2020-02-52'
        date5 = 20200101

        self.assertTrue(check_date(date1))
        self.assertFalse(check_date(date2))
        self.assertFalse(check_date(date3))
        self.assertFalse(check_date(date4))
        self.assertFalse(check_date(date5))

if __name__ == '__main__':
    unittest.main()
