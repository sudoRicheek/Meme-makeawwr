# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 02:18:38 2020

@author: Richeek Das
"""

from mememaker_editor import *
import os.path
import numpy as np
import cv2
from tkinter import *
from PIL import Image, ImageTk


##Buildit into a fucntion and access from other programss
class mememaker_gui(mememaker_editor) :
    
    font = None
    root = None
    usable_path = None
    usable_edit_path = None
    panel = None
    
    def __init__(self) :
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.usable_path = os.path.abspath("./") + "\\usable.jpg"
        self.usable_edit_path = os.path.abspath("./") + "\\usable_edit.jpg"
        
    def open_image(self, path_given) : 
        global root
        global usable_path
        """ Create window and import image and do relevant stuff for starting the program"""
        """ like creating a resized image and creating usable edits"""
        """One time execution"""

        root = Tk()
        root.title("Memeawwr")
        root.geometry('360x800')
        
        img_opened_in_opencv = cv2.imread(path_given, 1)
        shape_image = img_opened_in_opencv.shape
        newwidth = 250                                          
        """ Adjust According to root geometry """
        
        newheight = (int)((shape_image[0])/(shape_image[1]/newwidth))
        img_resized = cv2.resize(img_opened_in_opencv, (newwidth, newheight), interpolation = cv2.INTER_AREA)
        cv2.imwrite("usable.jpg", img_resized)      #Writes a scaled usable.jpg into the host directory of the backend file
        cv2.imwrite("usable_edit.jpg", img_resized) #Writes a scaled usable_edit.jpg into the host directory for editing purpose
        img = ImageTk.PhotoImage(Image.open(self.usable_path))       
        panel = Label(root, image = img)
        panel.grid(row = 0, column = 0, columnspan = 2)
                
    
    def create_buttons(self) :
        global root
        global panel
        obj_meme_editor = mememaker_editor()
        #Buttons
        Button1 = Button(root, text = "Gaussian Threshold", padx = 34, pady = 20, command = lambda: obj_meme_editor.gt(panel))
        Button2 = Button(root, text = " Black and White ", padx = 37, pady = 20, command = lambda: obj_meme_editor.bw(panel))
        Button3 = Button(root, text = " Saturation (+10) ", padx = 39, pady = 20, command = gt)
        Button31 = Button(root, text = " Text ", padx = 42, pady = 20, command = textt)
        Button4 = Button(root, text = "   Contrast(x2)  ", padx = 44, pady = 20, command = con1)
        Button41 = Button(root, text = "   Contrast(x0.5)  ", padx = 39, pady = 20, command = con2)
        Button5 = Button(root, text = "       Undo       ", padx = 52, pady = 20, command = gt)
        Button6 = Button(root, text = "    Begin Again   ", padx = 42, pady = 20, command = clear)
        
        
        #Packing Buttons
        txt = Label(root, text = ' ') ##For a space
        txt.grid(row = 1, column = 0, columnspan = 2)
        Button1.grid(row = 2, column = 0)
        Button2.grid(row = 2, column = 1)
        Button3.grid(row = 3, column = 0)
        Button31.grid(row = 4, column = 0)
        Button4.grid(row = 3, column = 1)
        Button41.grid(row = 4, column = 1)
        Button5.grid(row = 5, column = 0)
        Button6.grid(row = 5, column = 1)        
        
        root.mainloop()
        cv2.destroyAllWindows()
    
    
    
    
    