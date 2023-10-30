#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:58:56 2018

@author: Sergey Anfinogentov
"""


import fire
import glob
from astropy.io import fits
import numpy as np
import os
from magnify import magnify_motions_2d

def save_fits_to_dir(data, headers, out_dir, file_names):
    
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    nt = len(headers)
    nx = headers[0]['naxis1']
    ny = headers[0]['naxis2']

    for i in range(0,nt):
         hdu = fits.CompImageHDU(data[i,0:ny,0:nx], headers[i])
         file = os.path.join(out_dir, file_names[i])
         hdu.writeto(file, overwrite = True, output_verify="silentfix")

         


def read_fits_from_dir(fits_dir):
    files = glob.glob(fits_dir+"//*.fits")
    files.sort()
    nt = len(files)

    hdul = fits.open(files[0])

    #find hdu number with the image data
    im_ind = -2
    for i in range(len(hdul)):
        if hdul[i].header['naxis']==2:
            im_ind = i
            break
    if im_ind == -2:
        print("COuld not find image data")
        exit()


    hdu_data = hdul[im_ind]
    hdr =hdu_data.header
    
    nx =  hdr['naxis1']
    ny =  hdr['naxis2']
    nx0 = nx
    ny0 = ny
    if nx % 2 == 1:
        nx += 1
    if ny % 2 == 1:
        ny += 1
    
    data = np.zeros([nt, ny, nx])
    headers = []
    file_names = []
    
    for i in range(0,nt):
        hdul = fits.open(files[i])
        hdu_data = hdul[im_ind]
        hdu_data.verify('fix')
        data[i,0:ny0,0:nx0] = hdu_data.data[:,:]
        headers.append(hdu_data.header)
        file_names.append(os.path.basename(files[i]))
        
    return(data, headers, file_names)

def magnify_fits(input_dir, output_dir, k =4, width=70):

    #fits_dir = "//home//anfinogentov//data//aia_osc"

    #fits_out_dir = fits_dir +'_mag'

    print("Reading data...", end = ' ', flush = 1)
    data, headers, file_names =read_fits_from_dir(input_dir)
    print('DONE')
    data_mag = magnify_motions_2d(data, k = 4., width = 70)
    print("writing data...", end = ' ', flush = 1)
    save_fits_to_dir(data_mag, headers, output_dir, file_names)
    print('DONE')

if __name__ == '__main__':
  fire.Fire(magnify_fits)
