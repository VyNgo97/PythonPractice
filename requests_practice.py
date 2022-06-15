import requests
import json
import pandas as pd
import logging
import cProfile
import pstats

request_body = {'username': 'vyngo', 'password': 'password'}
URI = 'https://httpbin.org/'

def http_error(status_code):
    """This catches http error"""
    match status_code:
        case 200:
            logging.info("Request was successfully made.")
            return "OK"
        case 400:
            logging.info("Bad request")
            return "Bad Request"
        case 404:
            logging.info("Requested url not found.")
            return "Not found"
        case 403:
            logging.info("User not allowed to access this resource.")
            return "Forbidden"
        case 405:
            logging.info("Method not allowed")
            return "Method not allowed"

def post_request():
# using json instead of data sets content-type header to application/json
    try: 
        post_response = requests.post(URI, json=json.dumps(request_body))
        # can also use this to raise an error for 4xx or 5xx error rather than validating with http_error method
        post_response.raise_for_status()

    # generic error -> connection, timeout, etc
    except requests.RequestException as e:
        logging.error(f'Exception occurred while posting to {URI}')

    return post_response

# print(dir(r))
# print(r.text)
# print(r.status_code)

def main():
    response = post_request()
    http_error(response.status_code)

#     jsonBody = [
# 	{
# 		"color": "red",
# 		"value": "#f00"
# 	},
# 	{
# 		"color": "green",
# 		"value": "#0f0"
# 	},
# 	{
# 		"color": "blue",
# 		"value": "#00f"
# 	},
# 	{
# 		"color": "cyan",
# 		"value": "#0ff"
# 	}
# ]

    jsonBody = {
        "id": "0001",
        "type": "donut",
        "name": "Cake",
        "ppu": 0.55,
        "batters":
            {
                "batter":
                    [
                        { "id": "1001", "type": "Regular" },
                        { "id": "1002", "type": "Chocolate" },
                        { "id": "1003", "type": "Blueberry" },
                        { "id": "1004", "type": "Devil's Food" }
                    ]
            },
        "topping":
            [
                { "id": "5001", "type": "None" },
                { "id": "5002", "type": "Glazed" },
                { "id": "5005", "type": "Sugar" },
                { "id": "5007", "type": "Powdered Sugar" },
                { "id": "5006", "type": "Chocolate with Sprinkles" },
                { "id": "5003", "type": "Chocolate" },
                { "id": "5004", "type": "Maple" }
            ]
    }
    df = pd.json_normalize(jsonBody, max_level=2)
    # df = pd.read_json()
    print(df)

# with cProfile.Profile() as pr:
#     main()

# stats = pstats.Stats(pr)
# stats.sort_stats(pstats.SortKey.TIME)
# stats.print_stats()



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()