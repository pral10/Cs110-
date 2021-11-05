import stdio
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
small = min(x, y, z)
maximum = max(x, y, z)
medium = x+y+z-small-maximum
stdio.writeln(str(small) + ' ' + str(medium) + ' ' + str(maximum))
