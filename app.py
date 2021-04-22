from time import sleep
from phue import Bridge
import json
import requests
import os

# Load environment file, assign variables
from dotenv import load_dotenv
load_dotenv()

zd_user = os.environ["zendesk_username"]
zd_token = os.environ["zendesk_password"]
ticket_view_id = os.environ["ticket_view_id"]
hue_bridge_ip = os.environ["hue_bridge_ip"]
hue_light_name = os.environ["hue_light_name"]

## Hue Bridge and Light
b = Bridge(hue_bridge_ip)
light = hue_light_name

# If the app is not registered and the button is not pressed, press the button on your hue bridge and call connect() (this only needs to be run a single time)
b.connect()
get_bridge = b.get_api()

###Color map
color_map = {
    "red": [65280,0.6679,0.3181],
    "orange": [4547,0.5989,0.3779],
    "yellow": [1275,0.5425,0.4196],
    "green": [2443,0.1938,0.6821],
    "teal": [3958,0.1626,0.2774],
    "blue": [4692,0.1691,0.0441],
    "purple": [3958,0.1985,0.1037],
    "pink": [5610,0.4149,0.1776]
}

def set_color(color,light,brightness=None):
    if brightness:
        b.set_light(light, {"hue": color_map[color][0],
                            "xy": [color_map[color][1],
                                   color_map[color][2]],
                            "bri": brightness}
                )
    else:
        b.set_light(light, {"hue": color_map[color][0],
                            "xy": [color_map[color][1],
                                   color_map[color][2]]}
                )

# Reset color to purple; quick visual to know hue is connected and starting script.
set_color("purple",light)
sleep(1)
counter = 1
while True:
    url = 'https://objectrocket.zendesk.com/api/v2/views/44393853/count.json'
    get_ticket_view = requests.get(url, auth=(zd_user, zd_token))
    response_ticket_view = get_ticket_view.json()
    ticket_count = response_ticket_view['view_count']['value']
    if ticket_count < 10:
        set_color("green",light)
    elif ticket_count >= 10 or ticket_count <= 15:
        set_color("yellow",light)
    elif ticket_count > 15:
        set_color("red",light)
    print(f"loop has run, {str(counter)} times")
    counter += 1
    print("current ticket count is: " + str(ticket_count))
    print('''Sleeping for 15 seconds
    z
    zz
    zzz''')
    sleep(15)
