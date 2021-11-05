import stdio
import sys
# accept command line arguments m1,m2 and r as float.
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])
G = 6.674e-11
# formula for calculation the gravitational force
f = G*(m1*m2/r**2)
# writing the value of f to output
stdio.writeln(f)
