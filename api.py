import requests
import sys

def call_get(url: str) -> requests.models.Response:
    """
    Function that will call the API endpoint (input parameter) and return its response as a requests.models.Response object
    In case of an error, the program will exit and display the relevant message provided in the assignment brief
    """
    r = requests.get(url)
    if r.status_code == 200:
        return r
    else:
        print('There is an error with Frankfurter API')
