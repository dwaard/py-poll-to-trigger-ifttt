# importing the requests library 
import sys,os
import requests 
from dotenv import load_dotenv

project_folder = os.path.expanduser('')
load_dotenv(os.path.join(project_folder, '.env'))

def get_env(key):
    value = os.getenv(key)
    if not value:
        sys.exit("{key} not found in environment variables".format(key=key))
    return value

# # api-endpoint 
ifttt_key = get_env('IFTTT_WEBHOOK_KEY')
ifttt_event_name = get_env('IFTTT_WEBHOOK_EVENT_NAME')

IFTTT_URL = "https://maker.ifttt.com/trigger/{event}/with/key/{key}".format(event=ifttt_event_name, key=ifttt_key)

print(IFTTT_URL)

# # sending get request and saving the response as response object 
r = requests.get(url = IFTTT_URL) 