# importing the requests library 
import requests 

# api-endpoint 
URL = "https://maker.ifttt.com/trigger/dwaard_sent_request/with/key/UTRIYrT2PX4IKIdhrHigb"

# sending get request and saving the response as response object 
r = requests.get(url = URL) 
