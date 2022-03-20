# -*- coding: utf-8 -*-
"""
A QUIT button that verifies exit requests;
to reuse, attach an instance yo other GUIs, and re-pack as desired

-- FROM PROGRAMMING PYTHON --

Created on Sun Feb 20 08:18:09 2022

@author: dale
"""
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from tkinter import *
from tkinter.messagebox import askokcancel

class Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)
    
    def quit(self):
        ans = askokcancel('Verify Exit', 'Really Quit?')
        if ans: Frame.quit(self)

if __name__ == '__main__':
    Quitter().mainloop()