import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# numpy - numerical python - library for numerical calculations

xval = np.array([0,6,12])
yval = np.array([0,25, 75])

# plt.plot(xval, yval, color='darkgreen', marker='o', linestyle='dotted')
# plt.xlabel('Overs')
# plt.ylabel('Runs')
# plt.title('Team A Performance ')
# plt.grid(axis='y', linestyle='--', linewidth=0.5)
# plt.legend()
# plt.show()


overs = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 ])
teamA_runs = np.array([0,5,12,20,28,35,45,55,65,75,85,95,110,125,140,155,170,185,200,215,230])
teamB_runs = np.array([0,8,15,22,30,40,50,60,70,80,90,100,115,130,145,160,175,190,205,220,240])

plt.plot(overs, teamA_runs, marker='o', label='Team A', color='darkblue')
plt.plot(overs, teamB_runs, marker='x', label='Team B', color='darkred')
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title('Team A Performance ')
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
