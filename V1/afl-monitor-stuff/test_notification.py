import requests
import sys
import time
import sqlite3
import os
from pushover import init, Client
from datetime import datetime

pushnotify_key="NOTIFY_KEY_HERE" #hardcoded ftw
pushover_key="APP_API_KEY_HERE" #hardcoded ftw
init(pushnotify_key)

def test_notification(pushover_key):
        Client(pushover_key).send_message("Testing", title="Testing Message")
  
test_notification(pushover_key)
