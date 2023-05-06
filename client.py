import socket, win32clipboard ,sys ,os , pyperclip
sys.path.append(os.path.abspath("SO_site-packages"))
from PIL import ImageGrab,Image
import io
import tqdm
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
        
        clipboard_image = ImageGrab.grabclipboard()
        
        if clipboard_image is not None:
            
            image_file = "images/clipboard_image.png"

            file_size = os.path.getsize(image_file)

            clipboard_image.save(image_file)

            progress = tqdm.tqdm(range(file_size), "Sending clipboard_image", unit="B", unit_scale=True, unit_divisor=1024)

            with open(image_file,"rb") as image_file_rb:
            
                bytes_read  = image_file_rb.read()
                
                s.sendall(bytes_read)

                progress.update(len(bytes_read))

        else:

            recent_value = tmp_value
            #send text to the server
            s.send(str(recent_value).encode())
    #if data is received from the server
    data = s.recv(1024)
    if data:
         
         try:
                # Try to decode data as text
                text = data.decode('utf-8')
                pyperclip.copy(text)
                print(f"Copied text to clipboard: {text}")
         except UnicodeDecodeError:
                # If decoding as text fails, assume it's an image
                image = Image.open(io.BytesIO(data))
                pyperclip.copy('')
                image.save('images/clipboard_image.png')
                img = Image.open('images/clipboard_image.png')

                # create an in-memory file object to store the image data
                img_file = io.BytesIO()
                img.save(img_file, format='JPEG')
                img_data = img_file.getvalue()

                # copy the image data to the clipboard using the pyperclip library
                pyperclip.copy(img_data)
                

       

