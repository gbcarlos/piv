# -*- coding: utf-8 -*-
from matplotlib.pyplot import *
import numpy as np
from scipy import signal
import os

def loaddata(file1, file2):

    img1 = imread(os.path.realpath(file1))
    img2 = imread(os.path.realpath(file2))
    
    if img1.shape != img2.shape:
        raise ValueError('Dimensions of input images do not match!')
        
    if img1.ndim > 2:
        img1 = np.average(img1, axis=2)
        img2 = np.average(img2, axis=2)
    return img1, img2

x, y = loaddata('B005_1.tif', 'B005_2.tif')
imshow(x)

def piv(file1, file2, siw=20, ssw=None):
    #Init
    if np.size(ssw) < np.size(siw):
        raise ValueError('size_search_window zu klein')
    
    if ssw is None:
        ssw = siw
    
    #Load Images     
    img1, img2 = loaddata(file1, file2)
    sim1 = np.shape(img1) #size img
    
    #Grid with x and y vectors, x and y contain centers of each window
    x = np.arange(ssw//2, sim1[1], siw)
    y = np.arange(ssw//2, sim1[0], siw)
    X, Y = np.meshgrid(x, y)

    #Plot Grid
    #figure(3, figsize=(20,20))
    #plot(X, Y, marker='.', color='k', linestyle='none')
    #axis('equal')
    
    u = np.zeros((len(y), len(x)))
    v = np.zeros((len(y), len(x)))
    border_diffy = sim1[0] - y[-1]
    border_diffx = sim1[1] - x[-1]
    
    #Check border overflowing 
    if border_diffy < ssw//2 and border_diffy != 0:
        img1 = np.pad(img1, ((0, 0),(0, ssw//2 - border_diffy)))
    if border_diffx < ssw//2 and border_diffx != 0:
        img1 = np.pad(img1, ((0, ssw//2 - border_diffx),(0, 0)))
    
    for n,i in enumerate(x):
        for m,j in enumerate(y):
        
        #Window definition
            interr_window = np.array(img1[j-siw//2:j+siw//2, i-siw//2:i+siw//2])
            search_window = np.array(img2[j-ssw//2:j+ssw//2, i-ssw//2:i+ssw//2])
            
        #get correlation and index of spike
            interr_window = interr_window - np.mean(interr_window)
            search_window = search_window - np.mean(search_window)
            corr = signal.correlate2d(search_window, interr_window, mode='full')
            ind = np.unravel_index(corr.argmax(), corr.shape)
        
        #define u and v
            u[m, n] = ind[1] - ((ssw + siw)//2-1)
            v[m, n] = ind[0] - ((ssw + siw)//2-1)
            
                
    return X,Y,u,v

#"B005_1.tif", "B005_2.tif", "B_010.TIF","B_014.TIF" , "B038a.bmp", "B038b.bmp", "A001_1.tif", "A001_2.tif", 'A045a.tif', 'A045b.tif'

file1, file2 = "A001_1.tif", "A001_2.tif"
X, Y, U, V = piv(file1, file2, ssw=30)
M = np.sqrt(pow(U, 2) + pow(V, 2))

# Plot Results

#figure(figsize=(15,15))

#subplot(1,3,1)
#imshow(plt.imread(file2), alpha=.4)
#streamplot(X, Y, U, V)

#subplot(1,3,2)
#imshow(plt.imread(file2), alpha=.4)
#contourf(X,Y,M)

#subplot(1,3,3)
#imshow(plt.imread(file2), alpha=.4)
#quiver(X, Y, U, V, angles='xy')


