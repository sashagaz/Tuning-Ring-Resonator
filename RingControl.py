import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftshift
import numpy as np
from instrumental.drivers.daq.ni import NIDAQ, list_instruments
from scipy import signal 
print list_instruments()
import sys, select, os
import time


daq = NIDAQ('Dev1')

# Bias 0.427
time.sleep(1)

voltage = str(4) + 'V'
daq.ao0.write(voltage)
readFromAnalogImput8 = daq.ai0.read() 
print readFromAnalogImput8.magnitude - 0.427