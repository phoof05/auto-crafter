import random
import requests
import time
import json
import typing

# set up variables
element_list = {'Water', 'Fire', 'Wind', 'Earth'}
recipes: typing.Dict[str, typing.Tuple[str,str, str]] = {}
possible_combs = list(map(lambda i: list(map(lambda j: (i,j),element_list)), element_list))
possible_combs = [i for group in possible_combs for i in group]

# set up request obj
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://neal.fun/infinite-craft/',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'cookie' : 'cf_clearance=8NS2OdNhMMFW9DXvXGKey9aQ0Bq0aiSfxYQhd.UceTs-1710630112-1.0.1.1-b7uJlk2W.4Cn.sAbG4VjrPLuuZi1EpzgJkIaLvi.5gLzXwXrneFcSo34csJY5UnPHMHDKtOyPhUZ3Kbjg4cGrA; __cf_bm=U0_7aAfPhILhz2iBPkGEWMO.a9MNHCOe0a60qbwvcnc-1710631102-1.0.1.1-y8yjrAG.O0r7sTpYPIXYF4rLSm90BZcySWmSNlK6Jxo0B7DIAMGMpl5W0CfAyW6pffC85iqwPU7NgvAcpYkG1w'
    }

s = requests.Session()
done = False
while not done:
    index = random.randint(0, len(possible_combs) -1)
    curr_comb = possible_combs.pop(index)
    res = s.get(f'https://neal.fun/api/infinite-craft/pair?first={curr_comb[0]}&second={curr_comb[1]}', headers=headers).content.decode("utf-8")
    new_element = json.loads(res)["result"]
    isNew = json.loads(res)["isNew"]
    if new_element not in recipes.keys():
        recipes[new_element] = [(curr_comb[0], curr_comb[1])]
    else:
        recipes[new_element].append(curr_comb)
        
    if new_element not in element_list:
        element_list.add(new_element)
        possible_combs.extend([(new_element, i) for i in element_list])
    if isNew:
        done = True
    print (f'{new_element}: ---{curr_comb}---, ======{len(possible_combs)}====== ----new? {isNew}')
    time.sleep(.2)
print(recipes.keys())