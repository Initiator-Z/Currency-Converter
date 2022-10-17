import unittest
from currency import CurrencyConverter
from frankfurter import Frankfurter
from api import call_get

class TestCurrencyConverterInstantiation(unittest.TestCase):

    def test_instance(self):
        from_currency = 'AUD'
        to_currency = 'USD'
        date = '2021-01-01'
        cc = CurrencyConverter(from_currency, to_currency, date)

        self.assertEqual(cc.from_currency, from_currency)
        self.assertEqual(cc.to_currency, to_currency)
        self.assertEqual(cc.date, date)
        self.assertEqual(cc.amount, 1)
        self.assertEqual(cc.rate, None)
        self.assertEqual(cc.inverse_rate, None)
        self.assertEqual(str(type(cc.api)), str(type(Frankfurter())))

class TestCurrencyCheck(unittest.TestCase):

    def test_curr_true(self):
        from_currency = 'AUD'
        to_currency = 'GBP'
        date = '2021-01-01'
        cc = CurrencyConverter(from_currency, to_currency, date)
        result = cc.check_currencies()
        self.assertTrue(result)

    def test_curr_false_lower(self):
        from_currency = 'aud'
        to_currency = 'usd'
        date = '2021-01-01'
        cc = CurrencyConverter(from_currency, to_currency, date)
        result = cc.check_currencies()
        self.assertEqual(result, None)

    def test_curr_false_lower_single(self):
        from_currency = 'aud'
        to_currency = 'USD'
        date = '2021-01-01'
        cc = CurrencyConverter(from_currency, to_currency, date)
        result = cc.check_currencies()
        self.assertEqual(result, None)

    def test_curr_false_invalid(self):
        from_currency = 'abc'
        to_currency = '123'
        date = '2021-01-01'
        cc = CurrencyConverter(from_currency, to_currency, date)
        result = cc.check_currencies()
        self.assertEqual(result, None)

    def test_curr_false_invalid_single(self):
        from_currency = 'GBP'
        to_currency = '123'
        date = '2021-01-01'
        cc = CurrencyConverter(from_currency, to_currency, date)
        result = cc.check_currencies()
        self.assertEqual(result, None)

    def test_curr_false_length(self):
        from_currency = 'AUDa'
        to_currency = 'AU'
        date = '2021-01-01'
        cc = CurrencyConverter(from_currency, to_currency, date)
        result = cc.check_currencies()
        self.assertEqual(result, None)

    def test_curr_false_length_single(self):
        from_currency = 'AUD'
        to_currency = 'AU'
        date = '2021-01-01'
        cc = CurrencyConverter(from_currency, to_currency, date)
        result = cc.check_currencies()
        self.assertEqual(result, None)

    def test_curr_false_type(self):
        from_currency = 12
        to_currency = 12.12
        date = '2021-01-01'
        cc = CurrencyConverter(from_currency, to_currency, date)
        result = cc.check_currencies()
        self.assertEqual(result, None)

    def test_curr_false_type_single(self):
        from_currency = 'USD'
        to_currency = 12.12
        date = '2021-01-01'
        cc = CurrencyConverter(from_currency, to_currency, date)
        result = cc.check_currencies()
        self.assertEqual(result, None)

class TestReverseRate(unittest.TestCase):

    def test_rev_rate_int(self):
        from_currency = 'AUD'
        to_currency = 'USD'
        date = '2021-01-01'
        rate = 12

        cc = CurrencyConverter(from_currency, to_currency, date, rate)
        expected = round(1.0/rate, 4)
        result = cc.reverse_rate()
        self.assertEqual(result, expected)

    def test_rev_rate_float(self):
        from_currency = 'AUD'
        to_currency = 'USD'
        date = '2021-01-01'
        rate = 0.1225

        cc = CurrencyConverter(from_currency, to_currency, date, rate)
        expected = round(1.0/rate, 4)
        result = cc.reverse_rate()
        self.assertEqual(result, expected)

    def test_rev_rate_nagative(self):
        from_currency = 'AUD'
        to_currency = 'USD'
        date = '2021-01-01'
        rate = -0.23

        cc = CurrencyConverter(from_currency, to_currency, date, rate)
        expected = round(1.0/rate, 4)
        result = cc.reverse_rate()
        self.assertEqual(result, expected)

    def test_rev_rate_string(self):
        from_currency = 'AUD'
        to_currency = 'USD'
        date = '2021-01-01'
        rate = 'rate'

        cc = CurrencyConverter(from_currency, to_currency, date, rate)
        with self.assertRaises(TypeError):
            cc.reverse_rate()

class TestRoundRate(unittest.TestCase):

    def test_round_int(self):
        from_currency = 'AUD'
        to_currency = 'USD'
        date = '2021-01-01'
        rate = 1

        cc = CurrencyConverter(from_currency, to_currency, date)
        expected = 1
        result = cc.round_rate(rate)
        self.assertEqual(result, expected)

    def test_round_float(self):
        from_currency = 'AUD'
        to_currency = 'USD'
        date = '2021-01-01'
        rate = 1.12856

        cc = CurrencyConverter(from_currency, to_currency, date)
        expected = 1.1286
        result = cc.round_rate(rate)
        self.assertEqual(result, expected)

    def test_round_negative(self):
        from_currency = 'AUD'
        to_currency = 'USD'
        date = '2021-01-01'
        rate = -1.572988

        cc = CurrencyConverter(from_currency, to_currency, date)
        expected = -1.573
        result = cc.round_rate(rate)
        self.assertEqual(result, expected)

    def test_round_string(self):
        from_currency = 'AUD'
        to_currency = 'USD'
        date = '2021-01-01'
        rate = '-1.572988'

        cc = CurrencyConverter(from_currency, to_currency, date)
        with self.assertRaises(TypeError):
            cc.round_rate(rate)

class TestHistoricalRate(unittest.TestCase):

    def test_hist_rate(self):
        from_currency = 'AUD'
        to_currency = 'USD'
        date = '2021-01-01'

        cc = CurrencyConverter(from_currency, to_currency, date)
        info = call_get('https://api.frankfurter.app/2021-01-01?from=AUD&to=USD').json()
        expected_rate = info['rates'][to_currency]
        expected_inv_rate = 1.0/expected_rate
        rate, inv_rate = cc.get_historical_rate()
        self.assertEqual(rate, expected_rate)
        self.assertEqual(inv_rate, round(expected_inv_rate, 4))

if __name__ == '__main__':
    unittest.main()
