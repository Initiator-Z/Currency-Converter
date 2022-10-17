import unittest
from api import call_get

class TestAPI(unittest.TestCase):
    
    def test_callget(self):
        testurl = 'https://api.frankfurter.app/latest'
        result = call_get(testurl)
        self.assertEqual(str(type(result)), "<class 'requests.models.Response'>")

if __name__ == '__main__':
    unittest.main()
