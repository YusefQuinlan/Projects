# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:06:17 2020

@author: Yusef Quinlan
"""

import tkinter as tk
import winsound
import os
from scipy.io import wavfile
Window = tk.Tk()

def getText(aFile):
    print(aFile)
    Fs, x = wavfile.read(aFile)
    print('Duration: ', len(x)/Fs)
    winsound.PlaySound(aFile, 
        winsound.SND_FILENAME)
Path = str(os.getcwd())
for file in os.listdir(Path):
    if  (file.endswith(".wav")) :
        tk.Button(Window, text=file, command= lambda x=file: getText(x)).pack()
        tk.Label(Window).pack()


Window.mainloop()