import json
import os
import time
from datetime import datetime
from dotenv import load_dotenv

import requests

load_dotenv()

AZURE_KEY1 = os.environ['AZURE_KEY1']
# AZURE_KEY2 = os.environ['AZURE_KEY2']

data = {}
people = []

print('\nStarting\n')

reqUrl = "http://api.open-notify.org/astros.json"
response = requests.get(reqUrl)
json_response = response.json()

# Only put into json if everything's fine
if (response.status_code == 200) and json_response['message'] == 'success':
    print(f"Got data yeay\n")
    number = json_response['number']  # original response
    message = json_response['message']  # original response

    for item in json_response['people']:
        name = item['name']  # original response
        craft = item['craft']  # original response
        print('Adding {}'.format(name))
        bingReq = requests.get(
            'https://api.bing.microsoft.com/v7.0/images/search',
            headers={'Ocp-Apim-Subscription-Key': AZURE_KEY1},
            params={
                'q': name + ' astroanaut',
                'count': 1
            })
        if bingReq.status_code == 200:
            bingResponse = bingReq.json()
            people.append({
                'name':
                name,
                'craft':
                craft,
                'thumbnailUrl':
                bingResponse['value'][0]['thumbnailUrl'],
                'contentUrl':
                bingResponse['value'][0]['contentUrl']
            })
        else:
            raise RuntimeError(f"Status code {bingReq.status_code}")

        time.sleep(1)  # delay a bit

    # rebuild response
    data['data'] = {'people': people, 'number': number, 'message': message}

else:
    print(f'Failed ({response.status_code})')
    raise SystemExit()

fetch_finish = time.strftime("%a, %d %b %Y %H:%M %Z")  # format UTC Time
print(f'\nFetching finish at {fetch_finish}')

# writing all location data to file
with open('db.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)
    print('\nFinish writing to db.json')

log = {}
log['fetcher_last_run'] = fetch_finish

# writing log
with open('public/log.json', 'w') as outfile:
    json.dump(log, outfile, indent=2)
    print('Log is written to log.json')
