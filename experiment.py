"""
Task [I] - Demonstrating how to compute the histogram of an image using 4 methods.
(1). numpy based
(2). matplotlib based
(3). opencv based
(4). do it myself (DIY)
check the precision, the time-consuming of these four methods and print the result.
"""


import numpy as np
import matplotlib.pyplot as plt
from cv2 import cv2

###
#please coding here for solving Task [I].
# img=cv2.imread("D:\\pytest\\timg.jpg")
# B,G,R=cv2.split(img)#颜色通道分离
# cv2.imshow("RR",R)#只显示红色通道
# plt.hist(img[:,:,1].ravel(),bins=256,color='R')
# plt.xlabel('bins = 256 red levels')
# plt.ylabel('Counted pixel numbers in each level')
# plt.title('Red Histogram')
# plt.show()









###





"""
Task [II]Refer to the link below to do the gaussian filtering on the input image.
Observe the effect of different @sigma on filtering the same image.
Try to figure out the gaussian kernel which the ndimage has used [Solution to this trial wins bonus].
https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html
"""

###
#please coding here for solving Task[II]
import scipy
# from scipy import ndimage
# file_name = "D:\\pytest\\timg.jpg"
# imge= cv2.imread(file_name)
# cv2.imshow('gaussian.jpg',imge)
# imge1=ndimage.gaussian_filter(imge,sigma=10)
# plt.imshow(imge1)
# plt.show()
#sigma越大，越模糊








"""
Task [III] Check the following link to accomplish the generating of random images.
Measure the histogram of the generated image and compare it to the according gaussian curve
in the same figure.
"""

###
#please coding here for solving Task[III]
mean=[0,0]
cov=[[1,0],[0,1]]
x = np.random.multivariate_normal(mean, cov, (1000, 1000), 'raise')
plt.hist(x.ravel(), bins=256, color='g')
plt.show()
