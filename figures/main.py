import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from skimage.morphology import (
    binary_dilation,
    binary_erosion,
)


image = np.load("figures/TxtFiles/ps.npy")

labeled = label(image)

figure1 = np.array(
    [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
)

figure2 = np.array(
    [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1]]
)

figure3 = np.array(
    [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0], [1, 1, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1]]
)

figure4 = np.array(
    [[1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
)


figure5 = np.array(
    [[1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
)

figures = [figure1, figure2, figure3, figure4, figure5]

for figure in figures:
    erosed = binary_erosion(image, figure)
    dilation = binary_dilation(erosed, figure)
    image -= dilation
    print(label(dilation).max())

plt.title(f"Sum = {labeled.max()}")
plt.imshow(labeled)
plt.show()
