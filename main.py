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
def start():
    player = player_name.get()
    game_window = Toplevel(root)





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
frame_title.grid(row = 0, column = 0, columnspan = 3, padx = 25, pady = 25)

frame_image = Frame(root)
frame_image.grid(row = 1, column = 0, columnspan = 3, padx = 25, pady =25)

frame_name = Frame(root)
frame_name.grid(row = 2, column = 0, columnspan = 3, padx = 25, pady = 25)



#-- Place objects
# title
Label(frame_title, text = "Who wants to be a Millionaire?", bg = "Steel blue", font = ('Arial',16))\
    .grid(row=0, column = 1, padx = 0, pady = 0)

# Image
logo = PhotoImage(file="Millionaire.png")
Label(frame_image, image = logo)\
    .grid(row=0, column = 1, padx = 0, pady = 0)

# Name textbox and start button
Label(frame_name, text = "Name:", bg = "Steel blue")\
    .grid(row = 0, column = 0, padx = 0, pady = 0)
player_name = Entry(frame_name, width = 20, bg = "White")
player_name.grid(row = 0, column = 1, padx = 0, pady = 0)
start_button = Button(frame_name, text = "Start", width = 10, command = start)
start_button.grid(row = 0, column = 2, padx = 0, pady = 0)

#---- MAIN LOOP
root.mainloop()
