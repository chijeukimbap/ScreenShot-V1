from PIL import ImageGrab
from datetime import datetime
import keyboard

print("Screenshot running")
print("To take screenshot press | key ")
subject = input("Please enter subject: ")
topic = input("Please enter topic: ")
while True:
    try:
        
        if keyboard.is_pressed('|'):
            image = ImageGrab.grab()
            dt = datetime.now()
            fname = "{}_{}_{}.{}.png".format(subject,topic,dt.strftime("%H%M_%S"), dt.microsecond // 100000)
            image.save(fname, 'png')
            print(fname + " saved")


        else:
            pass
    except:
        break
       





