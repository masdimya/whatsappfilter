# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:31:48 2020

@author: ASUS
"""

import numpy as np 
import matplotlib.pyplot  as plt
from skimage import io
from skimage.transform import resize


def filter_img(filename):
    image_raw = io.imread("static/raw/"+filename)
    emoji     = io.imread("static/filter/filter.png")

    image = resize(image_raw, (500, 500),anti_aliasing=True)
    

    # image = image.astype('float')/255.
    emoji = emoji.astype('float')/255.


    mask = np.stack([emoji[:,:,3] for _ in range(3)], axis = 2)

    inv_mask = 1. - mask
    result = image * inv_mask + emoji[:,:,:3] * mask


    plt.imsave("static/img/"+filename,result)



