import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

data = np.random.randn(1500)
for i in range(len(data)):
    data[i] = data[i]*100


ax.hist(data, orientation='horizontal')
plt.show()