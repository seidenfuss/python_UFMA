import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('/home/ananeves/Documents/Github/python_UFMA/ana.jpeg')
imgplot = plt.imshow(img)
plt.show()

plt.imshow(img[:, :, 1], cmap="gray", vmin=0, vmax=255, interpolation="none")
plt.show()

plt.imshow(np.rot90(img))
plt.show()

plt.imshow(np.rot90(img, k=3))
plt.show()