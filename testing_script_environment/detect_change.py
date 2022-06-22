import time
import sys
import os
from numpy import byte
sys.path.append(os.path.abspath("SO_site-packages"))
import win32clipboard
import pyperclip

recent_value = None

# while True:
#     tmp_value = pyperclip.paste()
#     if tmp_value != recent_value:
#         recent_value = tmp_value
#         #determine the type of data that is copied
#         if type(recent_value) == str:
#             print("string")
#         elif type(recent_value) == int:
#             print("int")
#         elif type(recent_value) == bytes:
#             print("bytes")
#         print(recent_value)
#     time.sleep(0.1)


