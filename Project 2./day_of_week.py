import sys
import stdio
# taking m,d,y integer  as commandline arguments from user for getting month, day and year
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])
# using floored division to remove to fractional value
y0 = y-(14-m)//12
x0 = y0+y0//4-y0//100+y0//400
m0 = m+12*((14-m)//12)-2
dow = (d+x0+31*m0//12) % 7
# writing dow to standard output
stdio.writeln(dow)
