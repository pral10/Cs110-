import stdio
import sys
# accept n1,n2, integer and p  float as command line arguments.
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
p = float(sys.argv[3])

q = 1-p
p1 = (1-(p/q)**n2)/(1-(p/q)**(n1+n2))
p2 = (1-(q/p)**n1)/(1-(q/p)**(n1+n2))
# writing  p1 and p2 in output separated by space
stdio.writeln(str(p1) + ' ' + str(p2))
