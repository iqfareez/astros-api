import json
import time
from datetime import datetime
from zoneinfo import ZoneInfo

import requests

reqUrl = "http://api.open-notify.org/astros.json"

data = {}

print('\nStarting\n')

attempt_count = 0

# Retry if data still empty
while not data:
    if (attempt_count > 0):
        print(f'\nRetrying failed requests.\n')

    response = requests.get(reqUrl)
    json_response = response.json()

    # Only put into json if everything's fine
    if (response.status_code == 200) and json_response['message'] == 'success':
        print(f"Got data")
        data['astros'] = json_response
    else:
        print(f'Failed ({response.status_code})')

    attempt_count += 1

fetch_finish_utc = time.strftime("%a, %d %b %Y %H:%M:%S %Z")  # format UTC Time
print(f'Fetching finish at {fetch_finish_utc}')

# writing all location data to file
with open('db.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)
    print('\nFinish writing to db.json')

log = {}
log['fetcher_last_run'] = fetch_finish_utc

# writing log
with open('public/log.json', 'w') as outfile:
    json.dump(log, outfile, indent=2)
    print('Log is written to log.json')
