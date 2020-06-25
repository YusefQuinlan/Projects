First of all the folder Prior py files shows my progression to the final file.
And the main file 'PlaysoundsTkinterCompleted.py' is the completed file.
The main file essentially enables a user to play .wav files from the default folder that the
main file is run from, by clicking a button in a tkinter gui window. The gui will create list
items in a list box, and there is a scrollbar that allows a user to scroll up and down the listbox
when there are a large number of items. The list items are strings that are equivalent to the names of
the files in the directory from where the main file is run. If one selects a list item and then clicks the main
button, then the selected file/song/music will be played wia winsound.

The solution is far from perfect, some strange exception is triggered upon running this file, I have no
idea what causes this exception as I do not know everything about the way tkinter (the gui implemented)
is implemented. Another problem is that this only plays '.wav' files and that it only plays file that are
in the directory that the python file is run from. 

It is likely that there are other problems and uncaught errors that I have not seen, but the main thing is
that the program is functional and can play selected '.wav' files.
