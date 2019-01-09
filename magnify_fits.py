#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:58:56 2018

@author: Sergey Anfinogentov
"""


#from matplotlib import pyplot as plt
import magnify
import glob
from astropy.io import fits
import numpy as np
import os

def save_fits_to_dir(data, headers, out_dir, file_names):
    
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    nt = len(headers)

  
    
    for i in range(0,nt):
         hdu = fits.CompImageHDU(data[i,:,:], headers[i])
         file = os.path.join(out_dir, file_names[i])
         hdu.writeto(file, overwrite = True, output_verify="silentfix")

         


def read_fits_from_dir(fits_dir):
    files = glob.glob(fits_dir+"//*.fits")
    files.sort()
    nt = len(files)

    hdul = fits.open(files[0])
    hdu_data = hdul[1]
    hdr =hdu_data.header
    
    nx =  hdr['naxis1']
    ny =  hdr['naxis2']
    
    data = np.zeros([nt, ny, nx])
    headers = []
    file_names = []
    
    for i in range(0,nt):
        hdul = fits.open(files[i])
        hdu_data = hdul[1]
        hdu_data.verify('fix')
        data[i,:,:] = hdu_data.data[:,:]
        headers.append(hdu_data.header)
        file_names.append(os.path.basename(files[i]))
        
    return(data, headers, file_names)

fits_dir = "//home//sergey//data//kink_magnetic//limb2//fits"

fits_out_dir = fits_dir +'_mag'

print("Reading data...", end = ' ', flush = 1)
data, headers, file_names =read_fits_from_dir(fits_dir)
print('DONE')
data_mag = magnify.magnify_motions_2d(data, k = 4., width = 70)
print("writing data...", end = ' ', flush = 1)
save_fits_to_dir(data_mag, headers, fits_out_dir, file_names)
print('DONE')


