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



images_data = np.load('data/images_data.npy')
labels = np.load('data/labels.npy')


for i in np.random.randint(0, len(images_data), 7):
    plot(images_data[i,:,:], labels[i])

N = 10
indices = np.random.randint(0, len(images_data), [N,N])
fig, ax = plt.subplots(N, N, figsize=(8, 8))
for i in range(N):
        for j in range(N):
                ax[i,j].imshow(images_data[indices[i,j]].T, cmap = 'inferno' , origin='lower')
                ax[i,j].tick_params(left = False, right = False , labelleft = False ,
                        labelbottom = False, bottom = False)
plt.show()




print('\n',images_data.shape)

