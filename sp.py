#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:35:51 2016

@author: lihao
"""
# load module we write
import supplement as supp

# import other modules needed, install them if cannot found
import csv
import platform
import numpy as np
import random

if platform.system() == "Windows":
    datPath = "..\MATLAB\sp500_short_period.csv"
else:
    datPath = "../MATLAB/sp500_short_period.csv"

# read data from csv file
with open(datPath, newline='') as csvfile:
    csvData = csv.reader(csvfile)
    datList = []
    for row in csvData:
        datList.append(row)
        
# get the colnames in the first row and remove it
symbols = np.array(datList.pop(0))

# convert list to matrix
data = np.array(datList)
data = data.astype(np.float)
c = np.double((data[1:np.size(data, 0),:] - data[0:np.size(data, 0) - 1, :]) > 0)
movement = np.transpose(c)

K = 10  # 10 sectors so that 10 classes
max_iters = 1000 # maximum iterations
random.seed(1209)
idx = supp.km(movement, K, max_iters)


for k in range(K):
    print('\nStocks in group %d moving up together\n' % (k+1))
    k = np.array(k)
    index = np.squeeze(idx == k)
    print(symbols[np.where(index == True)])
    
      
            