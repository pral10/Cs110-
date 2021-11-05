import math
import stdio
import sys
# accept lat(latitude) as float with radian value and lone (longitude) float degree as command line
# argument
lat = math.radians(float(sys.argv[1]))
lone = float(sys.argv[2])

x = lone
y = (math.log((1+math.sin(lat))/(1-math.sin(lat))))/2

stdio.writeln(str(x) + ' ' + str(y))
