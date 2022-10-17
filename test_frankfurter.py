import unittest
from frankfurter import Frankfurter
from api import call_get

class TestUrl(unittest.TestCase):

    def test_url(self):
        frankfurter_base = 'https://api.frankfurter.app/latest'
        frankfurter_curr = 'https://api.frankfurter.app/currencies'
        frankfurter_hist = 'https://api.frankfurter.app/'
        frankfurter = Frankfurter()
        self.assertEqual(frankfurter_base, frankfurter.base_url)
        self.assertEqual(frankfurter_curr, frankfurter.currencies_url)
        self.assertEqual(frankfurter_hist, frankfurter.historical_url)

class TestCurrenciesList(unittest.TestCase):

    def test_curr_list(self):
        frankfurter = Frankfurter()
        result = frankfurter.get_currencies_list()
        expected = ['AUD','BGN','BRL','CAD','CHF','CNY','CZK','DKK','EUR','GBP','HKD','HRK','HUF','IDR','ILS','INR','ISK','JPY','KRW','MXN','MYR','NOK','NZD','PHP','PLN','RON','SEK','SGD','THB','TRY','USD','ZAR']
        self.assertEqual(result, expected)

class TestCheckCurrency(unittest.TestCase):

    def test_check_curr(self):
        true_currency = 'AUD'
        fake_currency1 = 'SSS'
        fake_currency2 = 'usd'
        fake_currency3 = 1.28
        fake_currency4 = True
        frankfurter = Frankfurter()
        self.assertTrue(frankfurter.check_currency(true_currency))
        self.assertFalse(frankfurter.check_currency(fake_currency1))
        self.assertFalse(frankfurter.check_currency(fake_currency2))
        self.assertFalse(frankfurter.check_currency(fake_currency3))
        self.assertFalse(frankfurter.check_currency(fake_currency4))

class TestHistoricalRate(unittest.TestCase):

    def test_hist_rate_object(self):
        frankfurter = Frankfurter()
        from_currency = 'AUD'
        to_currency = 'USD'
        from_date = '2021-01-01'
        result = frankfurter.get_historical_rate(from_currency, to_currency, from_date)
        self.assertEqual(str(type(result)), "<class 'requests.models.Response'>")

    def test_hist_rate_info(self):
        frankfurter = Frankfurter()
        from_currency = 'AUD'
        to_currency = 'USD'
        from_date = '2021-01-01'
        expected = call_get(f'https://api.frankfurter.app/{from_date}?from={from_currency}&to={to_currency}').json()
        result = frankfurter.get_historical_rate(from_currency, to_currency, from_date).json()
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
