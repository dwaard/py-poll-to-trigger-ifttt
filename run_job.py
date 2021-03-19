# importing the required libraries 
import sys,os
import requests 
from dotenv import load_dotenv


# load the environment variables
project_folder = os.path.expanduser('')
load_dotenv(os.path.join(project_folder, '.env'))


# Function that loads an environment variable or exits the program
# if the environment variable is not set properly
def get_env(key):
    value = os.getenv(key)
    if not value:
        sys.exit("{key} not found in environment variables"\
            .format(key=key))
    return value




# Create the IFTTT Webhook URL 
ifttt_key = get_env('IFTTT_WEBHOOK_KEY')
ifttt_event_name = get_env('IFTTT_WEBHOOK_EVENT_NAME')

IFTTT_URL = "https://maker.ifttt.com/trigger/{event}/with/key/{key}"\
    .format(event=ifttt_event_name, key=ifttt_key)


# sending the IFTTT webhook request 
print("Sending trigger to IFTTT event {}".format(ifttt_event_name))
r = requests.get(url = IFTTT_URL) 
if (r.ok):
    print("Success ({})".format(r.status_code))
else:
    print("IFTTT returned a response code {}, {}".format(r.status_code, r.reason))

