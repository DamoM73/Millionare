"""
Tkinter template
Comment here to descirbe what the program does.
Detail both the user inputs and the program outputs
"""

# import libaries
from tkinter import *

#---- CONSTANTS
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Who wants to be a Millionaire?"

#---- CLASSES

#---- FUNCTIONS ----

#-- General Functions --

#-- Functions executed when buttons are pressed --

#---- DRAW GUI
#-- Create a fixed size window ----
root = Tk()
root.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
root.title(SCREEN_TITLE)
root.wm_resizable(False, False)
root.configure(background = "Steel blue")

#-- Create frames for different sections
# copy the code below for each section in your GUI

frame_title = Frame(root)
frame_title.grid(row = 0, column = 0, columnspan = 1, padx = 25, pady = 25)

#-- Place objects


#---- MAIN LOOP
root.mainloop()
