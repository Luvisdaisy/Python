import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-8, 8, 1024)
y1 = 0.618 * np.abs(x) - 0.8 * np.sqrt(64 - x ** 2)
y2 = 0.618 * np.abs(x) + 0.8 * np.sqrt(64 - x ** 2)
plt.plot(x, y1, color='r')
plt.plot(x, y2, color='r')
plt.title("我爱C语言中文网",fontsize=20,color="b")
plt.show()