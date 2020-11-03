import sys,os
from astropy.table import Table, join, hstack

import astroFunctions as astro
import numpy as np
path_new = '/home/rafael/Projetos/DESzxcorr/results/viper_VVDS'

t = astro.joinTables(path_new,"PSPixelFit_PS1_VIPERS_VVDS.fits")
