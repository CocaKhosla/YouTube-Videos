import numpy as np
import imageio
import scipy.ndimage
import seaborn as sns
import matplotlib.pyplot as plt

# merges the two pictures together
def dodge(front,back):
    result=front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')


# function that converts image to black and white
def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


# enter image file
img ="file_name"


# image => b & w image => inverted image => gaussian filter => dodge (fancy stuff)
s = imageio.imread(img)
g = grayscale(s)
i = 255-g
b = scipy.ndimage.filters.gaussian_filter(i,sigma=40)
r= dodge(b,g)


# plotting => choose sns pallete that you want
fig, ax = plt.subplots()
my_cmap = sns.color_palette("Spectral", as_cmap=True)

ax.imshow(r, cmap=my_cmap)
plt.show()


# download photo and give it a name
plt.imsave('give_name', r, cmap=my_cmap, vmin=0, vmax=255)


 
