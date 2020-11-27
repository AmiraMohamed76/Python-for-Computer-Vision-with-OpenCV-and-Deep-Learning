#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 01:31:59 2020

@author: amira
"""
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image # this used to import image and convert it into array
pic = Image.open('DATA/00-puppy.jpg') # to import image
pic.show() # to show image
type(pic)
pic_arr = np.asarray(pic) # convert image into array
print(pic_arr.shape)
#plt.imshow(pic_arr) # to show image by converting the pixels to an image
pic_red = pic_arr.copy()
#plt.imshow(pic_red) 

""" R G B """ # here we will show each color channel of size (1300,1950,1)

""" Red channel values 0-225 """
#plt.imshow(pic_red[:, :, 0], cmap = 'gray') # cmap is color map we choose color gray 
                                            # 0 means No Color Value(pure black) & 225 means Full Color
""" Green channel values 0-225 """
#plt.imshow(pic_red[:, :, 1], cmap = 'gray')

""" Blue channel values 0-225 """
#plt.imshow(pic_red[:, :, 2], cmap = 'gray')

""" To get pure red image """
# Put green and blue channel = 0 same as for pure blue and green
pic_red[:, :, 1] = 0
pic_red[:, :, 2] = 0
plt.imshow(pic_red)


