
from datetime import datetime

from time import localtime

from playsound import playsound


current_date = datetime.now()


hour = datetime.strftime(current_date, '%H:%M')


print(current_date)


print(f'The time is {hour}!')


print('Please enter the hour and minute to set your alarm!')


h = input('hour :')


m = input ('minute:')


while True:

    if localtime().tm_hour == int(h) and localtime().tm_min == int(m):
        
        print('Alarm ringing!')

        
        Alarm = 'alarm.mp3'

        playsound(Alarm)
        
        
        break