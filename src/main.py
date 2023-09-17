"""
15/09/2023 10:50am ENE DANIELE
Main file
"""
from utils import compare, open_image
# from picamera import PiCamera
import time

print("⩹ PASS DETECTOR ⩺")
print("Make sure to use CTRL+C and `N` to allow the batch script to finish while stopping the main python script")
input("Press [ENTER] to take the idle picture, make sure nobody is in the frame")
# camera = PiCamera()
# camera.rotation = 180
# camera.capture('../images/idle.jpg')
idle = open_image("idle")  # IDLE PICTURE FROM CAMERA
tolerance = 0  # todo: figure out the right value here when you have something going on

while True:
    time.sleep(0.1)
    # ? TAKE A PICTURE AS images/frame.jpg
    if compare(idle, open_image("crazy")) > tolerance:
        print("hit the quan")
        # ? turn the LED on
    else:
        print("hit the griddy")
        # ? turn the LED off
    # ? os.remove("images/frame.jpg")

# ! AFTER ALL OF MY PAIN, AFTER ALL THAT IVE BECOME, WILL I DISAPPEAR?? DISAPPEAAAAAAAAAAAAAAAAAAR
# ? lorna shore phase?
