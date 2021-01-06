import numpy as np
from skimage import data
import matplotlib.pyplot as plt

img = io.imread('images/photoexample.jpg') # you can either load an image from folder
#img = data.camera()
#img[:10] = 0

# creating mask for an image 
mask = img < 87
img[mask] = 255
inds_x = np.arange(len(img))
inds_y = (4 * inds_x) % len(img)
img[inds_x, inds_y] = 0

l_x, l_y = img.shape[0], img.shape[1]
X, Y = np.ogrid[:l_x, :l_y]
outer_disk_mask = (X - l_x / 2)**2 + (Y - l_y / 2)**2 > (l_x / 2)**2
img[outer_disk_mask] = 0

plt.figure(figsize=(4, 4))
plt.imshow(img, cmap='black')
plt.axis('off')
plt.show()