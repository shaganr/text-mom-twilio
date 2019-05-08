import urllib3
import json
import os
http = urllib3.PoolManager()
r = http.request('GET', 'http://ipinfo.io/json')
data = json.loads(r.data.decode('utf-8'))
city=data['city']
loc=data['loc']
print(city,loc)
from twilio.rest import Client

client = Client(os.environ['SSID'], os.environ['AUTH'])
client.messages.create(to=os.environ['TO_NUM'],
                       from_=os.environ['FROM_NUM'],
body="hi amma i am in  "+city+"   now and my cordinates are  " +loc)