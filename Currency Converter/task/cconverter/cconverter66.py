import json
import requests


val_uta = input()
val_req = list(val_uta)

while val_req is not None:
    usd_or_eur = input()
    num = float(input())
    val_uta, usd_or_eur = val_uta.lower(), usd_or_eur.lower()
    # url2 = 'http://www.floatrates.com/json-feeds.html'
    req = requests.get(f"http://www.floatrates.com/daily/{val_uta}.json")
    req2 = req.json()
    # print(req2['usd']['rate'], '<--- USD')
    # print(req2['eur']['rate'], '<--- EUR')
    sum_rate = list()

    print('Checking the cache...')
    if req2 not in sum_rate:
        sum_rate.append(req2["{}".format(usd_or_eur)]['rate'])
        print(sum_rate, '<--- {}'.format(usd_or_eur))
        val = req2['{}'.format(usd_or_eur)]['rate']
        print(type(val), val)
        result = float(val * num)
        sum_dict = {usd_or_eur: val}

        print(sum_dict, 'DICTIONARY')
        print("Sorry, but it is not in the cache!")
        print("You received", round(result, 2), '{}'.format(usd_or_eur.upper()))

        sum_dict()
        print(sum_dict, "new dictionary")
    else:
        sum_rate.append(req2["{}".format(usd_or_eur)]['rate'])
        print('Oh! It is in the cache!')
        print("You received", round(result, 2), '{}'.format(usd_or_eur.upper()))
        if sum_rate not in sum_dict:
            sum_dict += sum_rate
            print(sum_dict)
    print(sum_rate)
