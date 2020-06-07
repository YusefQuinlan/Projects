# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:52:06 2020

@author: Yusef Quinlan
"""
# Only works on .wav files, but will play them all in alphabetical order.

import winsound
import os
from scipy.io import wavfile
import time
Path = str(os.getcwd())
for file in os.listdir(Path):
    if  (file.endswith(".wav")) :
        Fs, x = wavfile.read(file)
        print('Duration: ', len(x)/Fs)
        winsound.PlaySound(file, 
                   winsound.SND_FILENAME)
        time.sleep(len(x)/Fs)

