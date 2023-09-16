"""
15/09/2023 10:50am ENE DANIELE
Main file
"""
from utils import matrix, compare

print("\\\\\\ COLOMBETTI, ENE, KRIS, ETC IDRC: REGISTRO GALVANI \\\\\\")


input("Press [ENTER] to take the idle picture, make sure nobody is in the frame (it doesnt really matter though)")
#? TAKE A PICTURE AND SAVE ITS VALUES IN A MATRIX
idle = matrix("PICTURE GOES HERE")
tolerance = 0

while True:
    sleep(0.1)
    #? TAKE A PICTURE AS images/frame.jpg
    if compare(idle, matrix("frame")) > tolerance:
        #? hit the quan

#! AFTER ALL OF MY PAIN, AFTER ALL THAT IVE BECOME, WILL I DISAPPEAR?? DISAPPEAAAAAAAAAAAAAAAAAAR
#? lorna shore phase?
