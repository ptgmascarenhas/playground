"""
    Code to remove the background of png image
    Used to remove the backgoround of QR Code (white pixels)
"""

from PIL import Image
import numpy as np
import os

filename = "/cv/frame.png"
path = os.path.dirname(__file__)

img = Image.open(path + filename)
weigth, height = img.size
arr = np.array(img)

for i in range(0, weigth):
    for j in range(0, height):

        if arr[i,j,0] == 0:
            arr[i,j,0] = 255
            arr[i,j,1] = 255
            arr[i,j,2] = 255

        else:
            arr[i,j,0] = 0
            arr[i,j,1] = 0
            arr[i,j,2] = 0
            arr[i,j,3] = 0

img_new = Image.fromarray(arr, 'RGBA')
img_new.save(path + "/cv/new_frame.png")
img_new.show()

# print(arr[:,:,2])
