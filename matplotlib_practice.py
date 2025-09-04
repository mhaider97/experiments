import matplotlib.pyplot as plt
import numpy as np

img = np.random.rand(100, 100)  # fake image
plt.imshow(img, cmap="gray")
plt.show()