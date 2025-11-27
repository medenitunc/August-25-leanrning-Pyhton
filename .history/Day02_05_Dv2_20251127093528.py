import matplotlib.pyplot as plt
import numpy as np


# numpy - numerical python - library for numerical calculations

xval = np.array([0,6,12])
yval = np.array([0,250, 750])

plt.plot(xval, yval, color='darkgreen', marker='o', linestyle='dotted', label='Sales Data')
plt.show()

