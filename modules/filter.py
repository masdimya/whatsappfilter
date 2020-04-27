# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:31:48 2020

@author: ASUS
"""

import numpy as np 
import matplotlib.pyplot  as plt
from skimage import data


image = data.imread('sample_image.jpg')
emoji = data.imread('filter.png')

image_h, image_w, image_depth = image.shape

image = image.astype('float')/255.
emoji = emoji.astype('float')/255.


mask = np.stack([emoji[:,:,3] for _ in range(3)], axis = 2)

inv_mask = 1. - mask
result = image * inv_mask + emoji[:,:,:3] * mask


plt.imshow(result)



