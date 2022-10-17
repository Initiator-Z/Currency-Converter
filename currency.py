import sys
from frankfurter import Frankfurter

class CurrencyConverter:
    """
    Class that represents a Currency conversion object.
    It will be used to store the input arguments (currency codes, date) and also other information required (amount, rate, inverse rate, instantiation of Frankfurter class).
    """
    def __init__(self, from_currency, to_currency, date, rate=None, amount=1):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = amount
        self.rate = rate
        self.inverse_rate = None
        self.date = date
        self.api = Frankfurter()

    def check_currencies(self):
        """
        Method that will check if currency codes stored in the class attributes are valid.
        Otherwise the program will exit and display the relevant message provided in the assignment brief
        """
        if self.api.check_currency(self.from_currency) and self.api.check_currency(self.to_currency):
            return True
        elif self.api.check_currency(self.from_currency):
            print(f'{self.to_currency} is not a valid currency code')
        elif self.api.check_currency(self.to_currency):
            print(f'{self.from_currency} is not a valid currency code')
        else:
            print(f'{self.from_currency} and {self.to_currency} are not valid currency codes')

    def reverse_rate(self):
        """
        Method that will calculate the inverse rate from the value stored in the class attribute, round it to 4 decimal places and save it back in the class attribute inverse_rate.
        """
        reverse_rate = 1.0/self.rate
        return self.round_rate(reverse_rate)

    def round_rate(self, rate):
        """
        Method that will round an input argument to 4 decimals places.
        """
        rounded_rate = round(rate, 4)
        return rounded_rate

    def get_historical_rate(self):
        """
        Method that will call the Frankfurter API and get the historical conversion rate for the currencies (rounded to 4 decimals) and date stored in the class attributes.
        Then it will calculate the inverse rate and will exit by displaying the relevant message provided in the assignment brief
        """
        info = self.api.get_historical_rate(self.from_currency, self.to_currency, self.date, self.amount).json()
        self.rate = info['rates'][self.to_currency]
        inverse_rate = self.reverse_rate()
        print(f'The conversion rate on {self.date} from {self.from_currency} to {self.to_currency} was {self.rate}. The inverse rate was {inverse_rate}')
        return self.rate, inverse_rate
