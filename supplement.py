#!/usr/bin/python3

# import modules needed
import numpy as np

# k-means function
def km(X, K, max_iters):
    m, n = X.shape
    centroids = np.random.rand(K, n)
    idx = np.zeros((m, 1))
    idx = idx.astype(int)
    old_idx = np.zeros((m, 1))
    old_idx = old_idx.astype(int)
    
    for j in range(max_iters):
        change = False
        for i in range(m):
            foo = np.sum((np.tile(X[i,:], (K, 1)) - centroids)**2, axis = 1) 
            idx[i] = int(np.argmin(foo))
            if (idx[i] != old_idx[i]) and (change == False):
                change = True
        for k in range(K):
            k = np.array(k)
            index = np.squeeze(idx == k)
            centroids[k,:] = np.mean(np.squeeze(X[np.where(index == True), :]), axis = 0)
            
        if change == False:
            break
        
        old_idx = idx
       
    return idx
            
