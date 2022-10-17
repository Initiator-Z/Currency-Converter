import datetime
import sys

def check_arguments(args):
    """
    Function that will check if there are enough input arguments provided (ie exactly 3) and will return the input arguments if it is the case.
    Otherwise the program will exit and display the relevant message provided in the assignment brief
    """
    if len(args) == 3:
        return args
    else:
        print('[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>')
        sys.exit(0)

def check_date(date):
    """
    Function that will check if the provided date is valid and will return the value True if that is the case.
    Otherwise the program will exit and display the relevant message provided in the assignment brief
    """
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except:
        print('Provided date is invalid')
        sys.exit(0)
