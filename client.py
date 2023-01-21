import socket, win32clipboard ,sys ,os , pyperclip
sys.path.append(os.path.abspath("SO_site-packages"))

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
        data = data.decode()
        pyperclip.copy(data)
        
       

