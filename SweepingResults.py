import numpy as np
import matplotlib.pyplot as plt

voltage = list(np.linspace(0,2.4,13))
############
## Ring 1 ##
############

Current =[0.00, 0.01, 0.02, 0.04, 0.05, 0.06, 0.07, 0.08, 0.08, 0.09, 0.09, 0.10, 0.10]
P1_Wavelength =[1534.57, 1534.62, 1534.79, 1535.15, 1535.54, 1536.00, 1536.82, 1537.31, 1537.94, 1538.72, 1539.47, 1540.28, 1541.07]
P2_Wavelength =[1547.45, 1547.57, 1547.74, 1548.06, 1548.48, 1548.95, 1549.62, 1550.25, 1550.97, 1551.79, 1552.47, 1553.28, 1554.12]
P3_Wavelength =[1560.73, 1560.78, 1560.97, 1561.29, 1561.71, 1562.21, 1562.80, 1563.48, 1564.23, 1564.89, 1565.73, 1566.59, 1567.35]
P1_Power =[-44.259, -44.150, -43.876, -43.558, -43.080, -42.586, -42.298, -41.981, -41.780, -41.351, -41.030, -40.762, -40.415]
P2_Power =[-40.156, -40.212, -40.116, -40.112, -40.274, -40.270, -40.278, -40.562, -40.279, -40.397, -40.377, -40.180, -40.534]
P3_Power =[-40.454, -40.435, -40.490, -40.552, -40.604, -40.736, -41.212, -41.157, -41.542, -41.807, -42.520, -43.770, -44.842]

print len(P1_Wavelength),len(P2_Wavelength),len(P3_Wavelength)
plt.plot(voltage,P1_Wavelength,'r--',voltage,P2_Wavelength,'bs',voltage,P3_Wavelength,'g^')
plt.show()


############
## Ring 2  port 9 ##
############
#taking min trashold at -41.36 ; voltage = 0.00v on first ring

R2_Current = [0.000, 0.001, 0.002, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.009, 0.010, 0.010, 0.010]
R2_P1_Wavelength =[1533.33, 1533.41, 1533.59, 1533.88, 1534.93, 1535.14, 1535.70, 1536.29, 1537.00, 1537.83, 1538.59, 1539.45, 1540.28]
R2_P1_Power =[-48.010, -47.983, -48.231, -49.318, -51.732, -47.395, -45.120, -44.365, -43.802, -43.554, -43.083, -42.689, -42.366]
#when the voltage on ring2 is around 0.8, the influence from ring1 is huge. 'V' shape happens at 1534.45nm. 

R2_P2_Wavelength =[1546.33, 1546.37, 1546.58, 1546.85, 1546.92, 1548.08, 1548.62, 1549.32, 1550.13, 1550.80, 1551.63, 1552.43, 1553.31]
R2_P2_Power =[-42.754, -42.864, -43.444, -44.732, -48.002, -44.494, -42.849, -42.381, -42.459, -41.920, -42.087, - 42.167, -41.985]
#when the voltage on ring2 is around 0.8, the influence from ring1 is huge. 'V' shape happens at 1547.43nm. 

R2_P3_Wavelength =[1559.59, 1559.64, 1559.74, 1560.02, 1560.12, 1561.44, 1561.92, 1562.56, 1563.36, 1564.03, 1564.85, 1565.73, 1566.54]
R2_P3_Power =[-43.055, -43.144, -43.673, -44.985, -48.113, -44.903, -43.246, -42.922, -42.861, -42.955, -43.412, -44.073, -45.111]
#when the voltage on ring2 is around 0.8, the influence from ring1 is huge. 'V' shape happens at 1560.68nm.

plt.subplot(2,1,1)
plt.plot(voltage,R2_P1_Wavelength,'r--',voltage,R2_P2_Wavelength,'bs',voltage,R2_P3_Wavelength,'g^')
plt.ylabel('wavelength')

plt.subplot(2,1,2)
plt.plot(voltage,R2_P1_Power,'r--',voltage,R2_P2_Power,'bs',voltage,R2_P3_Power,'g^')
plt.ylabel('Optical Power')

plt.show()

###########Ring 3 port 5##############

Current =[0.000, 0.001, 0.002, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.009, 0.010, 0.010, 0.010]
R3_P1_Wavelength =[1528.77, 1528.35, 1528.48, 1528.77, 1529.04, 1530.20, 1530.57, 1530.76, 1531.87, 1532.96, 1533.14, 1534.12, 1535.41]
R3_P1_Power =[-36.033, -36.021, -36.087, -36.381, -37.745, -41.013, -40.356, -41.706, -43.975, -44.555, -44.307, -42.965, -40.240]

R3_p2_Wavelength =[1541.20, 1541.30, 1541.45, 1541.75, 1542.08, 1542.20, 1543.47, 1543.76, 1544.94, 1545.99, 1547.05, 1547.24, 1548.48]
R3_p2_power =[-38.590, -38.898, -39.097, -39.644, -41.200, -44.229, -44.358, -46.215, -48.440, -49.028,, -49.673, -48.097, -45.021]

R3_P3_Wavelength = [1554.49, 1554.52, 1554.61, 1554.96, 1555.27, 1555.42, 1556.86, 1557.01, 1588.26, 1559.30, 1560.30, 1561.55, 1561.75]
R3_P3_Power = [-44.237, -44.274, -44.763, -45.297, -47.048, -50.207, -51.176, -52.707, -54.300, -53.694, -52.642, -50.706, -46.273]

###########Ring 4 port 4##############


R4_Current = [0.000, 0.001, 0.002, 0.04, 0.05, 0.006, 0.007, 0.008, 0.008, 0.009, 0.009, 0.010, 0.010]
R4_P1_Wavelength =[1526.97, 1527.03, 1527.21, 1527.45, 1527.71, 1528.87, 1529.07, 1529.37, 1530.58, 1530.90, 1532.00, 1533.09, 1533.27]
R4_P1_Power =[-42.388, -42.236, -41.782, -41.479, -42.237, -44.682, -41.909, -43.715, -43.742, -44.719, -46.240, -47.513, -47.384]
#when the voltage on ring4 is around 1.0, the influence from ring1 is huge. 'V' shape starts from 1528.23nm. 

R4_P2_Wavelength =[1539.87, 1539.88, 1540.10, 1540.33, 1540.57, 1541.88, 1542.08, 1542.33, 1543.58, 1543.81, 1544.95, 1546.03, 1546.23]
R4_P2_Power =[-41.791, -41.813, -41.923, -42.480, -44.011, -47.414, -47.413, -45.250, -46.923, -47.249, -48.292, -50.538, -51.258, -51.969]


R4_P3_Wavelength =[1553.05, 1553.09, 1553.27, 1553.49, 1553.75, 1553.90, 1555.30, 1555.50, 1556.75, 1557.07, 1558.28, 1559.35, 1560.38]
R4_P3_Power =[-46.063, -46.146, -46.356, -46.993, -48.879, -51.946, -51.553, -53.706, -54.003, -55.417, -57.242, -55.979, -54.084]

