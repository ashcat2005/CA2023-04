"""
===============================================================================
This script produces shows the synthetic images of Kerr black holes.
===============================================================================
@author: Eduard Larrañga - 2023
===============================================================================
"""
#import warnings
#warnings.filterwarnings('ignore')

import numpy as np
import matplotlib.pyplot as plt


def plot(image_data, a, cmap='inferno'):
        '''
        Plots the image of the BH 
        '''
        ax = plt.figure().add_subplot(aspect='equal')
        ax.imshow(image_data.T, cmap = cmap , origin='lower')
        ax.set_xlabel(r'$\alpha$')
        ax.set_ylabel(r'$\beta$')
        plt.title('a = '+str(a))
        plt.tick_params(left = False, right = False , labelleft = False ,
                        labelbottom = False, bottom = False)
        plt.show()



images_data = np.load('images_data.npy')
labels = np.load('labels.npy')

print(images_data.shape)

for i in range(10):
    plot(images_data[i,:,:], labels[i])

print(images_data.shape)

