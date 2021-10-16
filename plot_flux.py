#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import sys

"""
 A simple routine to illustrate reading the csv file for the flux and making a plot.
"""

filename = 'flux.csv'
df = pd.read_csv(filename)  
df.insert(0, 'DATE_dt', pd.to_datetime(df['DATE'])) # convert dates to datetime objects 

key = '126.2-200.0'

fig = plt.figure(figsize=(12,5))

plt.plot(df['DATE_dt'], df[key], label=key)
plt.ylabel('Unsigned Flux ($10^{21}$ Mx)')
plt.legend()
plt.tight_layout()
plt.show()