try:
    import socket, win32clipboard ,time ,sys ,os , pyperclip
    sys.path.append(os.path.abspath("SO_site-packages"))
except:
    print('Please install win32clipboard and pyperclip')
    #wait for 5 seconds
    time.sleep(5)
    #exit if an error occur
    exit()
#text that is copied from the clipboard
recent_value = ""

#host
host = ''

#port
port  = 7777

#intialize connection
s = socket.socket()

#connect to the server
s.connect((host,port))

#running
running = True

while running:
    #detect if any changes in the clipboard
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        #send the data to the server
        s.send(str(recent_value).encode())
    #if data is received from the server
    data = s.recv(1024)
    if data:
        #send the data to the clipboard
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(data.decode())
        win32clipboard.CloseClipboard()
        #sleep
        time.sleep(0.1)     

