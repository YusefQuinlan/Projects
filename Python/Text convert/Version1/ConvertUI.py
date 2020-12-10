# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:15:02 2020

@author: Yusef Quinlan
"""

from tkinter import*
from tkinter import ttk
import os
import PyPDF2
from gtts import gTTS

#Make a main window
Main = Tk()
Main.title("ConvertPDFtoMp3")

#C:\Users\User\Downloads         so I can see my directory name for testing.

"""
 Saves and converts a chosen pdf file from a start point chosen by
 the user to an end point chosen by the user (i.e could be pages 6-18 of a pdf)
 this is so that users can skip contents pages or just take chapters. Saves 
 pdf as mp3 file in the same directory it is in, rather the directory that this
 file is run from.
"""
def save(FileAbsPath,Start,End):
    pdfOpen = open(FileAbsPath, 'rb')
    pdfRead = PyPDF2.PdfFileReader(pdfOpen)
    text = ""
    for i in range(int(Start.get()) -1,int(End.get()) ):
       text += pdfRead.getPage(i).extractText()
    Audio_file = gTTS(text=text, lang='en')
    Audio_file.save(FileAbsPath.replace(".pdf",".mp3"))

"""
    This makes a new window pop-up when the 'convert' button is pressed in the
    second window. And allows the third window generated to convert a selected
    pdf file given the start and end page
"""    
def convertBtn(Dir1,Listb):
    FileAbsPath = os.path.join(Dir1,Listb.get(Listb.curselection()))
    Name = Listb.get(Listb.curselection())
    Main3 = Tk()
    Main3.title("Choose conversion options for " + FileAbsPath)
    Label(Main3, text=" Conversion process for " + str(Name)).grid(row=0,column=0)
    Label(Main3, text="  ").grid(row=1,column=0)
    Label(Main3, text=" Below enter the number of the page you wish to start converting from").grid(row=2,column=0)
    Entry(Main3, width=80).grid(row=3,column=0)
    Label(Main3, text="").grid(row=4,column=0)
    Label(Main3, text="Below enter the number of the page you wish to end the conversion at").grid(row=5,column=0)
    Entry(Main3,width=80).grid(row=6,column=0)
    Start = Main3.grid_slaves(row=3,column=0)[0]
    End = Main3.grid_slaves(row=6,column=0)[0]
    Button(Main3,text="Convert",command=lambda z=FileAbsPath,y=Start,x=End: save(z,y,x)).grid(row=7,column=0)
    
    
"""
    Opens a second window when users click the directory button with a valid 
    directory as an argument in the entry widget of the main window, second
    window lists all the pdf files in that directory and allows users to 
    select pdfs to be converted (one at a time) in another window by the user.
"""
def getdir():
     # File not found error to be resolved or try-catched.
     Dir1 = Main.grid_slaves(row=1,column=0)[0].get()
     print(Dir1)
     Main2 = Tk()
     Main2.title("Select pdfs in directory: " + Dir1)
     F1 = Frame(Main2)
     scroller = Scrollbar(F1)
     Listb = Listbox(F1)
     scroller.pack(side=RIGHT, fill=Y)
     Listb.pack(side=LEFT, fill=Y)
     Listb.config(width=0)
     scroller['command'] = Listb.yview
     Listb['yscrollcommand'] = scroller.set
     for file in os.listdir(Dir1):
        if  (file.endswith(".pdf")) :
            Listb.insert(END, file)
     F1.pack(side=TOP)
     F2 = Frame(F1)
     Btn = Button(F2, text="Select",command=lambda z=Dir1,x = Listb: convertBtn(z,x))
     Btn.pack()
     F2.pack(side=TOP)
     Main2.mainloop()
     
"""
     Widgets in the main window.
"""
dirpromt = "Enter the directory path that contains pdfs you wish to convert"
dirbuttontxt = "Opens a window that allows conversion of all pdfs in a stated directory"
Label(Main, text=dirpromt).grid(row=0,column=0)
Entry(Main,width=140).grid(row=1,column=0)
Button(Main,text=dirbuttontxt,bg='blue',command=getdir).grid(row=2,column=0)
Main.mainloop()