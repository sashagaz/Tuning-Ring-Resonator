import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftshift
import numpy as np
from instrumental.drivers.daq.ni import NIDAQ, list_instruments
from scipy import signal 
print list_instruments()
import sys, select, os
import time

daq = NIDAQ('Dev1')

## Evaluate the time to execute the code
start_time = time.time()


#########################
## Write input voltage ##
#########################

## Write voltage from ao0 and read from ai8 ##

def writeVoltage(write):
    writeVoltage = str(write)+'V'
    daq.ao0.write(writeVoltage)
    readFromAnalogImput8 = daq.ai8.read()
    ai8 = readFromAnalogImput8.magnitude
    #print 'Analog Input 8: ',ai8 
    return write

	
write = writeVoltage(2.5)

##########################
## Read from Lorentzian ##
##########################

def getLorenValue(write):
    x = np.linspace(0.,9.9,500)
    mean = 1.5
    gamma = 1.
    noise = np.random.normal(1,.025,500)
    Lorentzian = (1/(1+np.square(2/gamma*(mean-x)))) *noise
    table = [x,Lorentzian]
    LorenValue = round(write*500/9.9)
    LorenVoltage = table[1][LorenValue]
    voltage = str(LorenVoltage) + 'V'
    daq.ao1.write(voltage)
    return LorenVoltage

voltage=4 
	
# Plot Lorentzian ##
x = np.linspace(0.,9.9,500)

mean = 1.5

gamma = 1.

noise = np.random.normal(1,.020,500)

Lorentzian = (1/(1+np.square(2/gamma*(mean-x)))) * noise

VoltageIndex = voltage *500 / 9.9

plt.plot(x,Lorentzian,voltage,Lorentzian[VoltageIndex],'ro')
plt.title("Lorentzian distribution with mean at %s and gamma of %s" %(mean,gamma))
plt.ylabel("Amplitude")
plt.xlabel("Voltage")
plt.show()
	
	
	
	
######################
## Keeping the Peak ##
######################

x1 = writeVoltage(0)
x2 = writeVoltage(2)

#print getLorenValue(3.5)


# x = 10
peak = 0

number_of_do_nothing = 0
number_of_steps = 0

while True:
    number_of_steps = number_of_steps + 1
    time.sleep(0.005)
    if getLorenValue(voltage*0.95)>getLorenValue(voltage*1.02):
        writeVoltage(voltage)
        voltage =voltage*.995
		
        print voltage
    elif getLorenValue(voltage*0.95)<getLorenValue(voltage*1.02):
        writeVoltage(voltage)
        voltage =voltage*1.010
        print voltage		
    else:
        number_of_do_nothing =  number_of_do_nothing +1
        print 'do nothing'	
        if number_of_do_nothing == 10:
            VoltageIndex = voltage *500 / 9.9
            plt.plot(x,Lorentzian,voltage,Lorentzian[VoltageIndex],'ro')
            plt.title("Lorentzian distribution with mean at %s and gamma of %s" %(mean,gamma))
            plt.ylabel("Amplitude")
            plt.xlabel("Voltage")
            plt.show()
            break

print number_of_steps
print "My program took", time.time() - start_time, "to run"
    
	
	
#while( getLorenValue(voltage) < getLorenValue(voltage*1.03) ):
#        voltage = writeVoltage(voltage*1.01)
#        print getLorenValue(voltage)

#getLorenValue(voltage)

# voltage = m *9.9 / 500
# print voltage