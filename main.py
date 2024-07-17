import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from PIL import Image


data = np.load(r"S2A_11SQA_20200415_0_L2A.npz")
im1 = data["gsd_10"]
im_natural_color = np.delete(im1, 3, 2)
im_infrared = np.delete(im1, np.s_[:3], 2)

plt.imshow(im_natural_color)
plt.show()

plt.imshow(im_infrared)
plt.show()
im = plt.imread("103956272.png")
plt.imshow(im)

plt.show()


image = Image.open('103956272.png')
splitted_channels = image.split()
print(splitted_channels)
plt.imshow(splitted_channels[0])
image_array = np.array(splitted_channels[0])

px_value_set = set([])
for col in image_array[:]:
    for value in col:
        px_value_set.add(value)

print(px_value_set)

plt.show()

plt.imshow(splitted_channels[1])

plt.show()

plt.imshow(splitted_channels[2])

plt.show()