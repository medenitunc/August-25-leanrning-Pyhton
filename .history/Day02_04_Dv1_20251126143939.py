import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('Day02_SampleData.csv')    
print(df)
plt.plot(df)
plt.show()