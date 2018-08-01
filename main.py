"""
Tkinter template
Comment here to descirbe what the program does.
Detail both the user inputs and the program outputs
"""

# import libaries
from tkinter import *

#---- Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Title"

#---- Functions executed when buttons are pressed ----


#---- Create a fixed size window ----
root = Tk()
root.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
root.Title = SCREEN_TITLE
root.wm_resizable(False, False)             # to resize, change to True (Width, Height)
root.configure(background = "Steel blue")   # refer to chart for available colour names

#---- Create frames for different sections

frame_one = Frame(root)
frame_one.grid(row = 0, column = 0, columnspan = 1, padx = 25, pady = 25)
