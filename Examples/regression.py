import numpy as np
import matplotlib.pyplot as plt
x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
z = np.polyfit(x, y, 3)
y_axis = np.poly1d(z)
x_axis = np.linspace(-2, 6, 100)
y_axis30 = np.poly1d(np.polyfit(x, y, 30))
plt.plot(x, y, '.', x_axis, y_axis(x_axis), '-', x_axis, y_axis30(x_axis), '--')
plt.ylim(-2,2)
plt.show()

from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x1 = np.linspace(0, 10, num=11, endpoint=True)
y1 = np.cos(-x1**2/9.0)
f1 = interp1d(x1, y1)

x2 = np.linspace(0, 10, num=41, endpoint=True)
y2 = f1(x2)
f2 = interp1d(x1, y1, kind='cubic')

plt.plot(x1, y1, 'o', x1, f1(x1), '-', x2, f2(x2), '--')

plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()