# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:28:52 2020

@author: Yusef Quinlan
"""

"""
Import tkinter because it is the gui that we build for the user to interface
to.   Import winsound because it is the package/module that plays '.wav' files.
Import os so that our operating system can get our current directory.
"""
import tkinter as tk
import winsound
import os

# Make a frame and add the scrollbar and listbox to it.
F1 = tk.Frame()
scroller = tk.Scrollbar(F1)
Listb = tk.Listbox(F1)

# pack the scrollbar and listbox on seperate lines because sometimes not doing
# so causes graphical glitches.

scroller.pack(side=tk.RIGHT, fill=tk.Y)
Listb.pack(side=tk.LEFT, fill=tk.Y)
Listb.config(width=0)
scroller['command'] = L.yview
Listb['yscrollcommand'] = s.set

# Get the directory path, i.e. the one we run this .py file from
Path = str(os.getcwd())

# Get all '.wav' files in our directory and add the names to our listbox.
for file in os.listdir(Path):
    if  (file.endswith(".wav")) :
        Listb.insert(tk.END, file)

"""Pack the main frame after everything has been added to it i.e. the scroller
  and the listbox. Put it at the top so that a second frame can be added
  underneath it and rendered seperately from this main frame.
  Create the playSound function that grabs curseselection 
  position and then gets the string of the position and plays the file with
  the same name as the retrieved string.
"""
F1.pack(side=tk.TOP)
def playSound():
    print(Listb.curselection())
    winsound.PlaySound(Listb.get(Listb.curselection()),
                       winsound.SND_FILENAME)

"""
Make a second frame seperate from the first to put our button into, the button
can then contain the playSound() function as a command so that users can select
a list item and click the button to play that file. Adding the Button to a
second frame below the TOP frame, allows the button to be visible and clickable
below the listbox and scroller.
"""    
F2 = tk.Frame()
Btn = tk.Button(F2, text="Play Audio", command=playSound)
Btn.pack()
F2.pack(side=tk.TOP)
tk.mainloop()