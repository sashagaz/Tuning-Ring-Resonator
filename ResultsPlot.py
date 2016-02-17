import matplotlib.pyplot as plt
import matplotlib.ticker as plt2
import numpy as np
from scipy import signal 
import time


biasVoltage = [0,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6]
wavelength = [1560.92,1561.02,1561.17,1561.53,1561.93,1562.44,1563.04,1563.7,1564.36,1565.17,1565.98,1566.61,1567.58,1568.4]

plt.plot(biasVoltage,wavelength,'r--o')
ax = plt.gca()
plt.title("Resonase shift versus input voltage")
plt.ylabel("Wavelength [nm]")
plt.xlabel("Voltage [V]")
y_formatter = plt2.ScalarFormatter(useOffset=False)
ax.yaxis.set_major_formatter(y_formatter)
plt.draw()
plt.show()