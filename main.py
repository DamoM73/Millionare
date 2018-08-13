"""
WHO WANTS TO BE A MILLIONAIRE
This program replicates the classic TV show using Tkinter GUI
"""

# import libaries
from tkinter import *

#---- CONSTANTS
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Who wants to be a Millionaire?"
BK_COLOUR = "Steel blue"


#---- CLASSES

#---- FUNCTIONS ----

#-- General Functions --

#-- Functions executed when buttons are pressed --

#---- DRAW GUI
#-- Create start window ----
root = Tk()
root.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
root.title(SCREEN_TITLE)
root.wm_resizable(False, False)
root.configure(background = BK_COLOUR)

#-- Create frames for different sections

# Title Frame
frame_title = Frame(root)
frame_title.grid(row = 0, column = 0, columnspan = 3, padx = 25, pady = 10)
frame_title.configure(bg= BK_COLOUR)

# Image Frame
frame_image = Frame(root)
frame_image.grid(row = 1, column = 0, columnspan = 3, padx = 25, pady = 10)

# Name & Start Frame
frame_start = Frame(root)
frame_start.grid(row = 2, column = 0, columnspan = 3, padx = 25, pady = 10)

#-- Place objects
Label(frame_title, text = "Who wants to be a Millionaire?", font = ('Arial',24), bg = BK_COLOUR)\
    .grid(row = 0, column = 1, padx = 0, pady = 0)

logo = PhotoImage(file="logo.gif")
Label(frame_image, bg = BK_COLOUR).image = logo


#---- MAIN LOOP
root.mainloop()
