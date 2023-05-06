import pyperclip
from PIL import ImageGrab

# get image from clipboard
clipboard_image = ImageGrab.grabclipboard()
image_in_clip  = False
def save_image():
    if clipboard_image is not None:
        # save image to file
        clipboard_image.save("clipboard_image.png")
        print("Image saved to clipboard_image.png")
        image_in_clip = True
    else:
        print("No image found on clipboard")



class image:
    def __init__(self) -> None:
        self.clipboard_image = ImageGrab.grabclipboard()
        self.image_in_clip  = False
               