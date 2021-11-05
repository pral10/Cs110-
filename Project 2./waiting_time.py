import math
import stdio
import sys
# here a= lambda
a = float(sys.argv[1])
t = float(sys.argv[2])
p = math.exp(-a*t)
stdio.writeln(p)
