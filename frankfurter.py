from api import call_get

#todo use call_get instead

class Frankfurter:
    """
    Class that manages API calls to Frankfurter. It will be used to store the URLS to the relevant endpoints. It will also automatically call the Currencies endpoint and store the return list of available currency codes.
    """
    def __init__(self):
        self.base_url = 'https://api.frankfurter.app/latest'
        self.currencies_url = 'https://api.frankfurter.app/currencies'
        self.historical_url = 'https://api.frankfurter.app/'
        self.currencies = call_get(self.currencies_url).json()

    def get_currencies_list(self):
        """
        Method that will get the list of available currencies and returns it as a Python list.
        """
        return list(call_get(self.currencies_url).json())

    def check_currency(self, currency):
        """
        Method that will check if a provided currency code is valid and return True if that is the case.
        Otherwise it will return False.
        """
        available_currencies = self.get_currencies_list()
        return (currency in available_currencies)


    def get_historical_rate(self, from_currency, to_currency, from_date, amount=1):
        """
        Method that will call the historical API endpoint in order to get the conversion rate for a given dates and currencies. It will return an requests.models.Response object.
        """
        historical_rate = call_get(f'{self.historical_url}{from_date}?from={from_currency}&to={to_currency}')
        return historical_rate
