import sys
from currency import CurrencyConverter
from checks import check_arguments, check_date

if __name__ == "__main__":
    args = sys.argv[1:]
    args = check_arguments(args)
    date = args[0]
    check_date(date)

    from_currency = args[1]
    to_currency = args[2]

    converter = CurrencyConverter(from_currency, to_currency, date)
    if converter.check_currencies():
        converter.get_historical_rate()
