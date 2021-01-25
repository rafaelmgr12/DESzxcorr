import  sys,os
from astropy.table import Table,join
import shutil
import astroFunctions as astro
import numpy as np
import healpy as hp

from astropy.table import Table, join, hstack,vstack,QTable
from esutil import htm
import numpy as np
import random
import sys
import os
import pandas as pd

path_tab = "/media/rafael/New HD/DES data/results/00028/pixel/vipers"
path_dir = "/media/rafael/New HD/DES data/64"
path_new = "/home/rafael/Projetos/DESzxcorr/results"

################################################################################################################
# Making an np.array of pixel of the
###############################################################################################################

filename = os.listdir(path_tab)
#des_filename = os.listdir(path_dir)
#des_pix = []
pix = []

for i in range(len(filename)):
    pix.append(int(filename[i][22:27]))
    #des_pix.append(int(des_filename[i][12:17]))

#des_pix = np.asanyarray(des_pix)
pix = np.asarray(pix)

#pix_neig = hp.get_all_neighbours(64,pix,nest = False,lonlat = True)
#pix_neig = pix_neig.reshape(-1,)


#################################################################################################################################################
# Concat now, in the previous filename
####################################################################################################################################
filename_1 = []
for i in range(len(pix)):
    filename_1.append("PixelFit_64_"+str(pix[i])+".fits")
totalF = filename_1 + filename 
#################################################################################################################################################
# Now take the numbe of the DES and compare
####################################################################################################################################
f = open("pix.txt","w")
for ele in totalF:
    f.write(ele+"\n")

for names in totalF:
    try:
        shutil.copyfile(os.path.join(path_dir,names),os.path.join(path_new,names))
    except:
        pass


#l = []
#for names in totalF:
#    try :
#        l.append(Table.read(os.path.join(path_dir,names)))
#    except :
#        pass        

#table = vstack(l)
#table.write("DES_PS.fits",overwrite = yes)
