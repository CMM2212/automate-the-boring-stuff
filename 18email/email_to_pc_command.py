import ezgmail
import datetime
import subprocess
from time import sleep

LAST_EMAIL_DATE = ezgmail.recent()[0].messages[0].timestamp



def check_email():
    global LAST_EMAIL_DATE
    if LAST_EMAIL_DATE == ezgmail.recent()[0].messages[0].timestamp:
        print('No new email detected')
        return
    
    LAST_EMAIL_DATE = ezgmail.recent()[0].messages[0].timestamp
    
    last_email = ezgmail.recent()[0].messages[0]
    sender = last_email.sender
    if 'run' in last_email.body:
        subprocess.Popen("C:\\Users\\mclea\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        print(f'Opened VS code from {last_email}')
        ezgmail.send(sender, 'Command Received', 'Command succesfully received, and opened VS Code')
    else:
        ezgmail.send(sender, 'Command Failed', f'Failed: {last_email.body!r} is not a valid command.')
        

while True:
    check_email()
    sleep(5)
    