# version 1.0
# created by Carlo Pasquinucci - carlo.a.pasquinucci@gmail.com
# relaesed under license GPL GNU 3 

### python file
### calculus of the reynolds number
### need sys.argv

### Run as python reynolds.py speed dimension material

import sys


speed=float(sys.argv[1])      # [m/s]
dimension=float(sys.argv[2])    # [m]
liquid=str(sys.argv[3]) 

print(str(speed))
print(str(dimension))
print(str(liquid))

if(liquid=="water"):
	density= 997  #[kg/m^3]
	cinVisco= 1*10**(-6)   # [m^2/s] (Air: 1.5e-05, Water: 1E-06 at room temp & pressure)
	dimVisco= density*cinVisco # [kg/m*s]

if(liquid=="air"):
	density= 1.225  #[kg/m^3]
	cinVisco= 1.5*10**(-5)   # [m^2/s] (Air: 1.5e-05, Water: 1E-06 at room temp & pressure)
	dimVisco= density*cinVisco # [kg/m*s]
	
	

re=speed*dimension/(cinVisco)

print(re)

if(re>8000):
	print("The flow is turbolent")
else:
	print("The flow is laminar")