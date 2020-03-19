# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:42:44 2020

@author: Richeek Das
"""

import os.path
import numpy as np
import cv2
from tkinter import *
from PIL import Image, ImageTk

class mememaker_editor(object) :

    usable_path = os.path.abspath("./") + "\\usable.jpg"
    usable_edit_path = os.path.abspath("./") + "\\usable_edit.jpg"
    preditbw = cv2.imread(usable_edit_path, 0)
    preditcol = cv2.imread(usable_edit_path, 1)

    ###################################
    #Begins the code for editing stuff#
    #preditbw is a bwimag             #
    #preditcol is an unchanged image  #
    ###################################

    def redefine_predits(self) :
        global preditbw
        global preditcol
        preditbw = cv2.imread(self.usable_edit_path, 0)
        preditcol = cv2.imread(self.usable_edit_path, 1)


    def apply_brightness_contrast(input_img, brightness = 0, contrast = 0):
        if brightness != 0:
            if brightness > 0:
                shadow = brightness
                highlight = 255
            else:
                shadow = 0
                highlight = 255 + brightness
            alpha_b = (highlight - shadow)/255
            gamma_b = shadow

            buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
        else:
            buf = input_img.copy()

        if contrast != 0:
            f = 131*(contrast + 127)/(127*(131-contrast))
            alpha_c = f
            gamma_c = 127*(1-f)

            buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

        return buf

    #Adaptive Gaussian Threshold
    def gt(self, panel):
        edit = cv2.adaptiveThreshold(self.preditbw, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)
        cv2.imwrite('usable_edit.jpg', edit)
        edit = ImageTk.PhotoImage(Image.open(self.usable_edit_path))
        panel.config(image = edit)
        panel.photo_ref = edit
        self.redefine_predits()

    def bw(self, panel):
        cv2.imwrite('usable_edit.jpg', self.preditbw)
        edit = ImageTk.PhotoImage(Image.open(self.usable_edit_path))
        panel.config(image = edit)
        panel.photo_ref = edit
        self.redefine_predits()

    def clear(panel):
    	global predit1
    	predit1 = cv2.imread(path, 1)
    	panel.config(image = img)

    def con1(panel):
    	global x
    	adjusted = apply_brightness_contrast(predit1, 0, x + 5)
    	x = x + 5
    	cv2.imwrite('editted.jpg', adjusted)
    	imgedit = ImageTk.PhotoImage(Image.open('editted.jpg'))
    	panel.config(image = imgedit)
    	panel.photo_ref = imgedit

    def con2(panel):
    	global x
    	adjusted = apply_brightness_contrast(predit1, 0, x - 5)
    	x = x - 5
    	cv2.imwrite('editted.jpg', adjusted)
    	imgedit = ImageTk.PhotoImage(Image.open('editted.jpg'))
    	panel.config(image = imgedit)
    	panel.photo_ref = imgedit

    def textt(panel):
    	i = 10
    	global predit1
    	while(1):
    		cv2.imshow('RUN TIME', predit1)
    		cv2.imwrite('editted.jpg', predit1)
    		k = cv2.waitKey(33)
    		imgedit = ImageTk.PhotoImage(Image.open('editted.jpg'))
    		panel.config(image = imgedit)
    		panel.photo_ref = imgedit
    		if k==27:    # Esc key to stop
    			cv2.waitKey(0)
    			cv2.destroyAllWindows()
    			break
    		elif k==-1:  # normally -1 returned,so don't print it
    			continue
    		else:
    			cv2.putText(predit1,chr(k),(i,50),font,1,(0,0,0),1,cv2.LINE_AA)
    			i+=15
