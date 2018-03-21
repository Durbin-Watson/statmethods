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