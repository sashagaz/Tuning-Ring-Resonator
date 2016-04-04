import matplotlib.pyplot as plt
import numpy as np
from instrumental.drivers.daq.ni import NIDAQ, list_instruments
print list_instruments()
import time
import msvcrt

daq = NIDAQ('Dev1')

#voltageRange = list(np.linspace(0,2.5,500))

def writeVoltage(voltage):
    voltage = str(voltage) + 'V'
    daq.ao0.write(voltage)  

def readVoltage():
    for time in range(1):
        readFromAnalogImput8 = daq.ai0.read() 
    return readFromAnalogImput8.magnitude - 0.377 ## bias

def gradient(x1,y1,x2,y2):
  x = (y2-y1)/(x2-x1)
  return x

initialVoltage = .2
voltageScaleUp = 1.03
voltageScaleDown = 0.97


flag_gradient = True

while True:

    writeVoltage(initialVoltage)
    VReadInitial = readVoltage()
    voltage = initialVoltage * 1.001
    writeVoltage(voltage)
    VReadfinal = readVoltage()

    gradient_starting  =  gradient(initialVoltage,VReadInitial,voltage,VReadfinal)



    if  gradient_starting > 0:
        
        gradient_left = gradient_starting
        
        while (flag_gradient): 
              print "Positive Gradient" 
              print voltage
              #Check that we are not exceeding maximum voltage in the ring
              if voltage > 2.5:
                  break

              if (gradient_left > 0):
                  
                  voltage = initialVoltage * voltageScaleUp
                  
                  writeVoltage(initialVoltage)
                  VReadInitial = readVoltage()

                  writeVoltage(voltage)
                  VReadfinal = readVoltage()          
                  gradient_left =  (VReadfinal-VReadInitial)/(voltage-initialVoltage)
                  initialVoltage = voltage

              else:

                  initialVoltage = voltage
                  flag_gradient = False
                  voltageRecord = VReadfinal
                  break

    else:
        
        gradient_right = gradient_starting
        
        while (flag_gradient): 
              print "Negative Gradient" 
              print voltage
              #Check that we are not exceeding maximum voltage in the ring
              if voltage > 2.5:
                  break

              if (gradient_right < 0):
                  
                  
                  voltage = initialVoltage * voltageScaleDown
                  
                  writeVoltage(initialVoltage)
                  VReadInitial = readVoltage()

                  writeVoltage(voltage)
                  VReadfinal = readVoltage()          
                  gradient_right =  (VReadfinal-VReadInitial)/(voltage-initialVoltage)
                  initialVoltage = voltage

              else:

                  initialVoltage = voltage
                  flag_gradient = False
                  voltageRecord = VReadfinal
                  break

    VReadfinal = readVoltage() 
    voltageDifference = np.abs(VReadfinal-voltageRecord)
    if voltageDifference > 0.1:
        flag_gradient = True
    else:
        print "locked"

    
    
    