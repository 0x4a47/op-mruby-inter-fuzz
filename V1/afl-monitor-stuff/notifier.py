# Notifier for new testcases
#
#   op-inter-fuzzv0.1
#
import pyinotify
import requests
import sys
import time
import sqlite3
import os
from pushover import init, Client
from datetime import datetime

#init stuffz
pushover_key="REDACTED" #hardcoded ftw
pushnotify_key="REDACTED" #hardcoded ftw
init(pushnotify_key)
print "[+] initializing..."
wm = pyinotify.WatchManager()  # Watch Manager
#watched events, we only care about file creation in the crashes folder
event_to_monitor = pyinotify.IN_CREATE
dir_to_monitor = "/root/other-stuff/test/"

def grab_file_content(file_path):
    print file_path
    f = open(file_path, 'r')
    f.seek(0)
    file_contents = f.read()
    print file_contents
    return file_contents

def send_notification(pushover_key, crash_file_path):
    message_body = "afl-fuzz-main found a new crash @" + str(datetime.now()) + "\n"
    message_body += "-------------------------------------------" + "\n"
    message_body += grab_file_content(crash_file_path) + "\n" #this is fiddly currently. Maybe omit
    message_body += "-------------------------------------------" + "\n"
    Client(pushover_key).send_message(message_body, title="afl-fuzz-main CRASH")

#self explanitory.
class EventHandler(pyinotify.ProcessEvent):
    #for the creation event.
    def process_IN_CREATE(self, event):
        print "[-] File Created:", event.pathname
        #send the notification XD
        print "[-] Sending notification..."
        send_notification(pushover_key, event.pathname)

#create the handler
handler = EventHandler()
#create the notifier with the watch manager
notifier = pyinotify.Notifier(wm, handler)
#add the directory we want to watch to the manager
wdd = wm.add_watch(dir_to_monitor, event_to_monitor, rec=True)
print "[+] beginning watch loop"

#start the loop
notifier.loop()
