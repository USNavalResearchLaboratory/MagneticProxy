#!/usr/bin/env python

import pandas as pd
import sys

if 'eve195' in sys.argv:
    filename = 'eve_fe_12_195.csv'
elif 'eve360' in sys.argv:
    filename= 'eve_fe_16_360.csv'
elif 'eve304' in sys.argv:
    filename = 'eve_he_02_304.csv'
elif 'f10' in sys.argv:
    filename = 'f10.csv'
elif 'flux' in sys.argv:
    filename = 'flux.csv'
elif 'pca' in sys.argv:
    filename = 'flux_pca.csv'
elif 'mg' in sys.argv:
    filename = 'mg.csv'
elif 'nro' in sys.argv:
    filename = 'nro.csv'
else:
    print(' ! no input specified, exiting . . .')
    exit()

df = pd.read_csv(filename)    
print(df)