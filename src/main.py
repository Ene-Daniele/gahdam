"""
15/09/2023 10:50am ENE DANIELE
Main file
"""
from utils import matrix, compare
import time

print("\\\\\\ COLOMBETTI, ENE, KRIS, ETC IDRC: REGISTRO GALVANI \\\\\\")


input("Press [ENTER] to take the idle picture, make sure nobody is in the frame (it doesnt really matter though)")
#? TAKE A PICTURE AND SAVE ITS VALUES IN A MATRIX
idle = matrix("PICTURE GOES HERE")
tolerance = 0  #todo: figure out the right value here when you have something going on

while True:
    time.sleep(0.1)
    #? TAKE A PICTURE AS images/frame.jpg
    if compare(idle, matrix("frame")) > tolerance:
        print("hit the quan")
        #? turn the led on
    else:
        print("hit the griddy")
        #? turn the led off

#! AFTER ALL OF MY PAIN, AFTER ALL THAT IVE BECOME, WILL I DISAPPEAR?? DISAPPEAAAAAAAAAAAAAAAAAAR
#? lorna shore phase?
