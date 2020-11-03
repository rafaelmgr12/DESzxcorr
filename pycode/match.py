import sys,os
from astropy.table import Table, join, hstack

import astroFunctions as astro
import numpy as np

name = []

# compute error for the mathcing
error = []
j = 1
while j < 3:
    #print(i,"\n")
    error.append(np.around(j/3600,5))
    j = j + 0.25

ps = Table.read('/home/rafael/Projetos/DESzxcorr/results/OzDES_GRC_2018_12_07.fits')
path_dir = '/home/rafael/Projetos/DESzxcorr/FITS/64'
path_new = '/home/rafael/Projetos/DESzxcorr/results'

for i,filename in enumerate(os.listdir(path_dir)):
    #print(filename)
    name = 'match_' + filename # aux variable to test it exist the file
    #print(name) # in a directory
    for k in range(len(error)):    
        if not astro.ver_file(path_new,name):# apply the test 
            file_ = Table.read(os.path.join(path_dir,filename))    
            data = astro.match(ps, file_,'RA','RA','DEC','DEC',error[k])
        if len(data) != 0:
            data.add_column(1.5, name = 'random')
            for i in range(0, len(data)):
                data[i]['random'] = np.random.random()
    #if len(data['RA']) != 0:
	aux = str(error[k])
	aux = aux[2:]
        filename = 'match_' + aux + "_" + filename 
        name.append(filename)
        data.write(os.path.join(path_new,filename))

for i in name:
    t = astro.joinTables(path_new,i+".fits")

#astro.joinTables1(path_new,'match.fits')  #if the first function doesn't work
