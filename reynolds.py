# version release 1.0
# created by Carlo Pasquinucci - carlo.a.pasquinucci@gmail.com
# relaesed under license GPL GNU 3
# please, read the disclaimer at https://github.com/Carlopasquinucci/General_disclaimer/releases


### python file
### calculus of the reynolds number
### need sys.argv

### Run as python reynolds.py speed dimension material

import sys

help=' Reynolds Calculator. Run as python reynolds.py speed dimension material. As material you can choose water or air.'

# check import
if len(sys.argv) < 4:
	print(' Some arguments are missing ')
	print(help)
	exit(1)
if len(sys.argv) > 4:
	print(' Too arguments are present ')
	print(help)
	exit(1)

if not(sys.argv[1].replace('.','',1).isdigit() and sys.argv[2].replace('.','',1).isdigit()):
	print(' The first two arguments MUST be numbers. ')
	print(help)
	exit(1)
if not(sys.argv[3]=='water' or sys.argv[3]=='air'):
	print(' The third argument MUST be air or water. ')
	print(help)
	exit(1)


speed=float(sys.argv[1])      # [m/s]
dimension=float(sys.argv[2])    # [m]
liquid=str(sys.argv[3]) 

print(' For this speed: '+str(speed))
print(' this dimension: +'+str(dimension))
print(' and this material: '+ str(liquid))

if(liquid=="water"):
	density= 997  #[kg/m^3]
	cinVisco= 1*10**(-6)   # [m^2/s] (Air: 1.5e-05, Water: 1E-06 at room temp & pressure)
	dimVisco= density*cinVisco # [kg/m*s]

if(liquid=="air"):
	density= 1.225  #[kg/m^3]
	cinVisco= 1.5*10**(-5)   # [m^2/s] (Air: 1.5e-05, Water: 1E-06 at room temp & pressure)
	dimVisco= density*cinVisco # [kg/m*s]
	
	

re=speed*dimension/(cinVisco)

print('The reynolds number is:' + str(re))

if(re>8000):
	print("The flow is turbolent")
else:
	print("The flow is laminar")
