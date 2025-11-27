import matplotlib.pyplot as plt
import numpy as np


# numpy - numerical python - library for numerical calculations

xval = np.array([0,6,12])
yval = np.array([0,25, 75])

plt.plot(xval, yval, color='darkgreen', marker='o', linestyle='dotted')
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title('Team A Performance ')
plt.grid()
plt.show()