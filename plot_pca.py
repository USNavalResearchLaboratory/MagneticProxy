#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

"""
 A simple routine to illustrate reading the csv file for the pca components and making a plot.
"""

filename = 'flux_pca.csv'
df = pd.read_csv(filename)  
df.insert(0, 'DATE_dt', pd.to_datetime(df['DATE'])) # convert dates to datetime objects 

key = 'pc1'

fig = plt.figure(figsize=(12,5))

plt.plot(df['DATE_dt'], df[key], label=key)
plt.ylabel('Component Magnitude')
plt.legend()
plt.tight_layout()
plt.show()