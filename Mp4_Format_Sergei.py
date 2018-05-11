#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 10:11:19 2018

@author: Katie Kosak
## CFSA, Warwick University
### Uses Dr. Sergei Anfinogentov's Motion Magnification Code
### This code enables the use of MP4 or AVI formats with the code
"""

from magnify import *
import cv2
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import animation

## Animation Settings ############
Writer = animation.writers['ffmpeg']
writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=180)

# Have  a mp4 file converted into a data cube ##################
cap = cv2.VideoCapture('baby.mp4')
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

input_data = np.empty((frameCount, frameHeight, frameWidth,3), np.dtype('double'))
fc = 0
ret = True

while (fc < frameCount  and ret):
    ret, input_data[fc] = cap.read()
    fc += 1

cap.release()

############### Convert RGB Data to 1 Color Stream ################
input_data=np.sum(input_data,axis=3)
###################### MOtion Magnification ###########################
k= 5 #Magnification
width= 80 # width
result = magnify_motions_2d(input_data, k, width)



################# Save the Movie as mp4 ##################


def Create_Animation(image,number_of_files,title):
    ## Create an Array of pictures from a Data Cube
    images=[]
    fig=plt.figure()
    for i in range(number_of_files):
        img_plot=plt.imshow(image[i])   
        images.append([img_plot])
    ani = animation.ArtistAnimation(fig, images, interval=100, blit=True)
    ani.save(title,writer=writer)
    return images
    
images=Create_Animation(result,frameCount,'baby_result.mp4')

