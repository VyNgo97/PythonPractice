import requests


import requests
import json
import pandas as pd
import logging
import pprint

URI = 'https://cat-fact.herokuapp.com/facts'
dict_data =     {
        "id": "4",
        "model": "Surface Pro 6",
        "disk_space": "256GB",
        "screen_size": "13in",
        "details": {
            "screen-type": "led",
            "price":"$999.00",
            "supports": ["vga", "hdmi", "dp"]
            }
    }

pp = pprint.PrettyPrinter(indent=4)

def parse_list():
    r = requests.get(URI)

    # r.content returns byte type
    # print(type(r.content))
    
    # response.text is string type- do we want to work on it as a string or a list/dict?
    logging.info(f'Response type: {type(r.text)}')

    # this will convert to a list or dict depending on the structure of the json response
    data = json.loads(r.text)
    pp.pprint(data)

    # TODO: print only the "text" field of each object in the list
    clean_list = [(idx,item["text"]) for idx, item in enumerate(data)]
    print(len(clean_list))
    pp.pprint(clean_list)

def parse_from_file():
    with open('data.json', 'r') as file:
        data = file.read()
    obj = json.loads(data)
    return obj

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    # parse_list()
    print(parse_from_file()["details"])