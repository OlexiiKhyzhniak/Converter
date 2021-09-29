import requests


def check_success(url):
    r = requests.get(url).status_code
    if r == 200:
        return 'Success'
    else:
        return 'Fail'
