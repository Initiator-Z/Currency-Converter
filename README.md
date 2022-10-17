# Currency Converter

Convert popular currencies with command line input. Based on Frankfurter API.

## Getting Started

### Installing

* Simply clone or download the files in your chosen directory

### Executing program

* Execute the program by running:
```
python main.py \
  --<date> \
  --<Original Currency> \
  --<Target Currency> \
```
As an example, the following command requests the conversion rate(and inverse rate) from Australian Dollar to Japanese Yen on 2021/03/12

<python main.py 2021-03-12 AUD JPY>

## List of available currency codes
* AUD: Australian Dollar
* BGN: Bulgarian Lev
* BRL: Brazilian Real
* CAD: Canadian Dollar
* CHF: Swiss Franc
* CNY: Chinese Renminbi Yuan
* CZK: Czech Koruna
* DKK: Danish Krone
* EUR: Euro
* GBP: British Pound
* HKD: Hong Kong Dollar
* HRK: Croatian Kuna
* HUF: Hungarian Forint
* IDR: Indonesian Rupiah
* ILS: Israeli New Sheqel
* INR: Indian Rupee
* ISK: Icelandic Króna
* JPY: Japanese Yen
* KRW: South Korean Won
* MXN: Mexican Peso
* MYR: Malaysian Ringgit
* NOK: Norwegian Krone
* NZD: New Zealand Dollar
* PHP: Philippine Peso
* PLN: Polish Złoty
* RON: Romanian Leu
* SEK: Swedish Krona
* SGD: Singapore Dollar
* THB: Thai Baht
* TRY: Turkish Lira
* USD: United States Dollar
* ZAR: South African Rand

## Program Structure
* api.py: Function to call corresponding api based on given url
* checks.py: Checks the validity of input arguments from user
* currency.py: Class that gets, stores and manipulates conversion rates based on given arguments
* frankfurter.py: Class that gets and stores required inforamtion from Frankfurter api
* main.py: Extracts input arguments and calls currency converter class to obtain and dsiplay conversion results
* test_api.py: Test the functioning of api.py regarding response object type
* test_checks.py: Test checks.py regarding formating of arguments
* test_currency.py: Test currency.py regarding valid and invalid input arguments
* test_frankfurter.py: Test frankfurter.py regarding consistency of information obtained from Frankfurter api
