import time
import os
import datetime
from sense_hat import SenseHat
import json, requests

sense = SenseHat()
sense.low_light = True
sense.set_rotation(270) # Optional
sense.clear()

# Get the weather-api
key = '9b5766921f34cdb5e1b1f4acbe105c53'
units = 'metric'
#units = 'imperial'
cityid = '2622418'
url = requests.get('http://api.openweathermap.org/data/2.5/weather?id='+cityid+'&units='+units+'&APPID='+key)
weather = json.loads(url.text)

print (weather['main']['temp'])
print (weather['weather'][0]['description'])
print (weather['weather'][0]['main'])

weathre = weather['weather'][0]['description']
temp = weather['main']['temp']
main_weather = weather['weather'][0]['main']

update_weather_delay = 50   # Delay between updating the weather data
update_weather = update_weather_delay

# Display Clock, Date, etc.
show_clock = True
show_month = True
show_temp = True
show_weathre = True
show_mail = False

number = [
0,1,1,1, #zero
0,1,0,1,
0,1,0,1,
0,1,1,1,
0,0,1,0, #one
0,1,1,0,
0,0,1,0,
0,1,1,1,
0,1,1,1, #two
0,0,1,1,
0,1,1,0,
0,1,1,1,
0,1,1,1, #three
0,0,1,1,
0,0,1,1,
0,1,1,1,
0,1,0,1, #four
0,1,1,1,
0,0,0,1,
0,0,0,1,
0,1,1,1, #five
0,1,1,0,
0,0,1,1,
0,1,1,1,
0,1,0,0, #six
0,1,1,1,
0,1,0,1,
0,1,1,1,
0,1,1,1, #seven
0,0,0,1,
0,0,1,0,
0,1,0,0,
0,1,1,1, #eight
0,1,1,1,
0,1,1,1,
0,1,1,1,
0,1,1,1, #nine
0,1,0,1,
0,1,1,1,
0,0,0,1
]

hourColour   = [255,0,0] # red
minuteColour = [255,128,0] # yellow
empty        = [0,0,0] # off / black

clockImage = [
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0
    ]

e = (0,0,0)

clear = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]

b = (66, 134, 244)
r = (255, 0, 50)

cloudy = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,b,e,e,e,
    e,b,e,b,e,b,b,e,
    b,e,b,e,e,e,e,b,
    b,e,e,e,e,e,e,b,
    e,b,b,b,b,b,b,e,
    e,e,e,e,e,e,e,e
    ]

thermo = [
    e,e,e,e,e,e,e,e,
    e,e,r,e,r,r,r,e,
    e,e,r,e,e,e,e,e,
    e,e,r,e,r,r,e,e,
    e,e,r,e,e,e,e,e,
    e,r,e,r,e,e,e,e,
    e,e,r,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]

def clock():
    now = datetime.datetime.now()
    second = now.second
    x = 0
    y = 7
    r = 255
    g = 0
    b = 0
    pixel = (r,g,b)

    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min

    # Map digits to clockImage array

    pixelOffset = 0
    index = 0
    for indexLoop in range(0, 4):
        for counterLoop in range(0, 4):
            if (hour >= 10):
                clockImage[index] = number[int(hour/10)*16+pixelOffset]
            clockImage[index+4] = number[int(hour%10)*16+pixelOffset]
            clockImage[index+32] = number[int(minute/10)*16+pixelOffset]
            clockImage[index+36] = number[int(minute%10)*16+pixelOffset]
            pixelOffset = pixelOffset + 1
            index = index + 1
        index = index + 4

    # Colour the hours and minutes

    for index in range(0, 64):
        if (clockImage[index]):
            if index < 32:
                clockImage[index] = hourColour
            else:
                clockImage[index] = minuteColour
        else:
            clockImage[index] = empty

    # Display the time
    sense.set_pixels(clockImage)
    sense.set_pixel(x, y, pixel)
    time.sleep(0.5)
    sense.set_pixels(clockImage)
    #sense.set_pixels(clear)
    time.sleep(0.5)
    #time.sleep(.3)

def month():
    now = datetime.datetime.now()
    second = now.second
    x = 0
    y = 7
    r = 255
    g = 0
    b = 0
    pixel = (r,g,b)

    mday = time.localtime().tm_mday
    mon = time.localtime().tm_mon

    # Map digits to clockImage array

    pixelOffset = 0
    index = 0
    for indexLoop in range(0, 4):
        for counterLoop in range(0, 4):
            clockImage[index] = number[int(mday/10)*16+pixelOffset]
            clockImage[index+4] = number[int(mday%10)*16+pixelOffset]
            clockImage[index+32] = number[int(mon/10)*16+pixelOffset]
            clockImage[index+36] = number[int(mon%10)*16+pixelOffset]
            pixelOffset = pixelOffset + 1
            index = index + 1
        index = index + 4

    # Colour the hours and minutes

    for index in range(0, 64):
        if (clockImage[index]):
            if index < 32:
                clockImage[index] = minuteColour
            else:
                clockImage[index] = hourColour
        else:
            clockImage[index] = empty

    # Display the time
    sense.set_pixels(clockImage)
    time.sleep(4.0)

print ('Ready!')

while (True):
    if show_mail:
        os.system('sudo python /home/pi/SenseHat/Sense_CheckMail.py')

    if show_clock:
        for x in range(2):
            for x in range(8):
                clock()
            if show_month:
                month()

    if show_weathre:
        sense.set_pixels(cloudy)
        time.sleep(1.0)
        sense.show_message(str(weathre), text_colour=[66, 134, 244])
        time.sleep(0.3)

    if show_temp:
        sense.set_pixels(thermo)
        time.sleep(1.0)
        sense.show_message(str(temp), text_colour=[255, 0, 50])
        time.sleep(0.3)

    if update_weather == 0:
        url = requests.get('http://api.openweathermap.org/data/2.5/weather?id='+cityid+'&units='+units+'&APPID='+key)
        weather = json.loads(url.text)
        weathre = weather['weather'][0]['description']
        temp = weather['main']['temp']
        main_weather = weather['weather'][0]['main']
        update_weather = update_weather_delay
        print("- Weather updated successfully -")
    else:
        update_weather -=1