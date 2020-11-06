#############################################################################################################
# This code make the match with the optical data, in a way to make this very quickly 
# and optimize
#
#############################################################################################################

import  sys,os
from astropy.table import Table,join

import astroFunctions as astro
import numpy as np
import healpy as hp

##############################################################################################################
#Important variables to make the in the code
##############################################################################################################

#tabName = []

# compute te error in the error for the matching 
error = []
j = 1
while j < 3:
    error.append(np.around(j/3600,5))
    j = j + 0.25
error = np.asarray(error)

path_tab = "/home/rafael/Projetos/DESzxcorr/results/viper_vvds"
path_dir = "/home/rafael/Projetos/DESzxcorr/FITS/64"
path_new = "/home/rafael/Projetos/DESzxcorr/results"

################################################################################################################
# Making an np.array of pixel of the
###############################################################################################################

filename = os.listdir(path_tab)
#des_filename = os.listdir(path_dir)
#des_pix = []
pix = []

for i in range(len(filename)):
    pix.append(int(filename[i][12:17]))
    #des_pix.append(int(des_filename[i][12:17]))

#des_pix = np.asanyarray(des_pix)
pix = np.asarray(pix)

pix_neig = hp.get_all_neighbours(64,pix,nest=True,lonlat=True   )
pix_neig = pix_neig.reshape(-1,)

#################################################################################################################################################
# Concat now, in the previous filename
####################################################################################################################################
filename_1 = []
for i in range(len(pix_neig)):
    filename_1.append("PixelFit_64_"+str(pix_neig[i])+".fits")
totalF = filename_1 + filename 
#################################################################################################################################################
# Now take the numbe of the DES and compare
####################################################################################################################################
for filenames in filename:
    for k in range(len(error)):
        aux = str(error[k])
        aux = aux[2:]
        for names in totalF:
            test = 'match_' + aux + '_' + names
            if not astro.ver_file(path_new,test):
                try:
                    file_ = Table.read(os.path.join(path_dir,names))
                    ps = Table.read(os.path.join(path_tab,filenames))
                    data = astro.match(ps, file_,'raMean','RA','decMean','DEC',error[k])
                    if len(data) != 0 :
                        data.add_column(1.5, name = 'random')
                        for i in range(0, len(data)):
                            data[i]['random'] = np.random.random()
    #if len(data['RA']) != 0:
                    names = 'match_'+aux+'_'+names
                    #tabName.append(names)
                    data.write(os.path.join(path_new,names))
                except:
                    pass