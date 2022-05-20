import time
import sys
import os
sys.path.append(os.path.abspath("SO_site-packages"))

import pyperclip

recent_value = ""
while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        print("Value changed: %s" % str(recent_value)[:20])
    time.sleep(0.1)

def copy():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    print(data)