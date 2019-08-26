import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('screenshot.png')

plt.imshow(img)
plt.show()


