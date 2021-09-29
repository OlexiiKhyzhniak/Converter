import requests
import json

val_uta = input()
val_req = list(val_uta)
cache = dict()

while val_req is not None:
    usd_or_eur = input()
    num_str = input()
    val_uta, usd_or_eur = val_uta.lower(), usd_or_eur.lower()
    # url2 = 'http://www.floatrates.com/json-feeds.html'
    req = requests.get(f"http://www.floatrates.com/daily/{val_uta}.json")
    req2 = req.json()
    # print(req2['usd']['rate'], '<--- USD')
    # print(req2['eur']['rate'], '<--- EUR')

    if usd_or_eur == "":
        break
    else:
        num = float(num_str)

    val_rate = req2['{}'.format(usd_or_eur)]['rate']
    val = req2['{}'.format(usd_or_eur)]['code']

    # print('VAL ------->', val)
    # print('VAL_RATE -->', val_rate)

    currency_rates = {usd_or_eur: val_rate}
    # print(currency_rates, '--> currency_rates (ТЕКУЩАЯ ВАЛЮТА)')
    cache['usd'], cache['eur'] = val_rate, val_rate
    # print(cache, "КЭШ")
    if usd_or_eur in cache.keys():
        # print(cache.keys())
        print('Checking the cache...')
        print('Oh! It is in the cache!')
        # print(val_rate)
        # print(cache)
        # print(type(cache))
        val_rate = cache[usd_or_eur]
        result2 = float(val_rate * num)
        print("You received", round(result2, 2), '{}'.format(usd_or_eur.upper()) + '.')
    elif currency_rates[usd_or_eur] not in cache.keys():
        # print(cache.keys())
        cache[usd_or_eur] = val_rate
        val_rate = cache[usd_or_eur]
        result = float(val_rate * num)
        # print(cache, "--> cache (КЭШ)")
        print('Checking the cache...')
        print('Sorry, but it is not in the cache!')
        print("You received", round(result, 2), '{}'.format(usd_or_eur.upper()) + '.')
