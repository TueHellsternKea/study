import time
import os

hour = int(input('Enter hours '))
minute = int(input('Enter minutes '))
second = int(input('Enter seconds '))

time = hour*10800 + minute*3600 + second*60

print('{}:{}:{}'.format(hour,minute,second))

while time > 0:
   time = time - 1
   seconds = (time // 60) % 60
   minutes = (time // 3600)
   hours = (time // 10800)
   print('Time  ',hours,':',minutes,':',seconds,)
   os.system("CLS")                                  