# write your code here!
import requests
import json

currency = input().lower()
r = requests.get(f'http://www.floatrates.com/daily/{currency}.json')
json_string = r.text
currency_dict = json.loads(json_string)
cache = dict()

if currency == 'usd':
    cache['eur'] = currency_dict['eur']['rate']
elif currency == 'eur':
    cache['usd'] = currency_dict['usd']['rate']
else:
    cache = {
        'usd': currency_dict['usd']['rate'],
        'eur': currency_dict['eur']['rate']
    }
while True:
    currency_exchange = input().lower()
    if currency_exchange == '':
        break
    else:
        amount_money = float(input())
        if currency_exchange in cache.keys():
            print('Checking the cache...')
            print('Oh! It is in the cache!')
            result = amount_money * cache[currency_exchange]
        else:
            print('Checking the cache...')
            print('Sorry, but it is not in the cache!')
            result = amount_money * currency_dict[currency_exchange]['rate']
        cache[currency_exchange] = currency_dict[currency_exchange]['rate']
        print(f'You received {round(result, 2)} {currency_exchange.upper()}.')


