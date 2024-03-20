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
    }

s = requests.Session()
done = False
while not done:
    random.shuffle(possible_combs)
    curr_comb = possible_combs.pop(0)
    res = s.get(f'https://neal.fun/api/infinite-craft/pair?first={curr_comb[0]}&second={curr_comb[1]}', headers=headers).content.decode()
    print(res)
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
    print (f'{res}: ---{curr_comb}---, ======{len(possible_combs)}====== ----new? {isNew}')
    time.sleep(.175)
print(recipes.keys())