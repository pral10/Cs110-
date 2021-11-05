import stdio
import stdrandom
import sys

# Accept an Integer  command line
n = int(sys.argv[1])
# use stdrandom.uniform to get random side for n roll of dice
x = stdrandom.uniformInt(1, n+1)
x += stdrandom.uniformInt(1, n+1)
# writing value of x to output
stdio.writeln(x)
