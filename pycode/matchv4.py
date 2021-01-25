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

# compute te error in the error for the matching
choice = eval(input(
    "Compute the distance using in the matching, \n Type 1 for the varying distance\n Else for fixed.\n\n"))

if choice == 1:
    print("Here the error ranging from 1 to 2.75 arcsec\n\n")
    error = []
    j = 1
    while j < 3:
        error.append(np.around(j/3600, 5))
        j = j + 0.25
    error = np.asarray(error)
    print("Under Constructions")
    exit()
else:
    error = eval(input("Type the distance in arcsec: \n"))
    error = np.around(error/3600, 5)
print("-"*200)\
################################################################################################################################################################################################################################
# Directory paths
################################################################################################################################################################################################################################
path_tab = "/home/rafael/Projetos/DESzxcorr/results/PSPixelFit_PS1_VIPERS_VVDS"
path_dir = "/home/rafael/Projetos/DESzxcorr/FITS/64"
path_new = "/home/rafael/Projetos/DESzxcorr/results/match-des-ps2"
################################################################################################################################################################################################################################
des_filename = os.listdir(path_tab)
#ps_filename = os.listdir(path_tab)

for des in range(len(des_filename)):
    list_pixel  = []
    list_pixel.append(des_filename[des])
    pixel = int(des_filename[des][12:17])
    pix_neig = astro.get_neigbours(64,pixel)
    for ps in range(len(pix_neig)+3):
        try:
            list_pixel.append("PixelFit_64_"+str(pix_neig[ps])+".fits")
            des_tab = Table.read(os.path.join(path_dir, des_filename[des]))
            ps_tab = Table.read(os.path.join(path_tab, list_pixel[ps]))
            #print("Match of the DES file ", des_filename[des], "\n")
            #print("Match of the PS file ", list_pixel[ps], "\n")
            if des_filename[des] == list_pixel[0]:
                data = astro.match(ps_tab, des_tab, 'raMean',
                                   'RA', 'decMean', 'DEC', error)
            else:
                aux = vstack(data, astro.match(
                    ps_tab, des_tab, 'raMean', 'RA', 'decMean', 'DEC', error))
                data = aux.copy()
            if len(data) != 0 :
                data.add_column(1.5, name = 'random')
                for i in range(0, len(data)):
                    data[i]['random'] = np.random.random()
            name = "match_" + des_filename[des]
            print("\n", name, "\n Save")
            data.write(os.path.join(path_new, name)) 
        except:
            print("Do not exist files")
            pass