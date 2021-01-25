#############################################################################################################
# This code make the match with the optical data, in a way to make this very quickly
# and optimize
#
#############################################################################################################

import sys
import os
from astropy.table import Table, join, vstack

import astroFunctions as astro
import numpy as np
import healpy as hp

##############################################################################################################
# Important variables
##############################################################################################################

#print("Here the error ranging from 1 to 2.75 arcsec\n\n")
error = []
j = 1
while j < 4:
    error.append(np.around(j/3600, 5))  
    j = j + 0.25
error = np.asarray(error)


################################################################################################################################################################################################################################
# Directory paths
################################################################################################################################################################################################################################
path_tab = "/home/rafael/Projetos/DESzxcorr/results/PSPixelFit_PS1_VIPERS_VVDS"
path_dir = "/home/rafael/Projetos/DESzxcorr/FITS/64"
path_new = "/home/rafael/Projetos/DESzxcorr/results/match-des-ps"
################################################################################################################################################################################################################################
# Compute the match of 1 pixel
des_filename = os.listdir(path_tab)

for j in range(len(error)):
    aux1 = str(error[j])
    aux1 = aux1[2:]
    list_pixel  = []
    list_pixel.append(des_filename[0])
    pixel = int(des_filename[0][12:17])
    pix_neig = astro.get_neigbours(64,pixel)
    for ps in range(len(pix_neig)+3):
        try:
            list_pixel.append("PixelFit_64_"+str(pix_neig[ps])+".fits")
            des_tab = Table.read(os.path.join(path_dir, des_filename[0]))
            ps_tab = Table.read(os.path.join(path_tab, list_pixel[ps]))
            print("Match of the DES file ", des_filename[0], "\n")
            print("Match of the PS file ", list_pixel[ps], "\n")
            if des_filename[0] == list_pixel[0]:
               data = astro.match(ps_tab, des_tab, 'raMean',
                                   'RA', 'decMean', 'DEC', error[j])
            else:
                aux = vstack(data, astro.match(
                    ps_tab, des_tab, 'raMean', 'RA', 'decMean', 'DEC', error[j]))
                data = aux.copy()
            
            name = "match_"+ aux1 + "_" + des_filename[0]
            print("\n", name, "\n Save")
            data.write(os.path.join(path_new, name)) 
        except:
            print("Do not exist files")
            pass