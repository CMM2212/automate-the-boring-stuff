import ezgmail
import os
import datetime
from time import sleep

while datetime.datetime.now().hour in [10,11,12]:
    print(datetime.datetime.now())
    sleep(10)
    

ezgmail.send('7012009579@messaging.sprintpcs.com', '', 'It is now 1 in the afternoon')

print(f'Sent text at {datetime.datetime.now()}')