import pandas   as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Day02_SampleData.csv')
data.plot()
plt.show()