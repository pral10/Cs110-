import stdarray
import stdrandom
import stdio

# create a 2D list minuet with dimension (11 , 16) and filling the array with minuet measures
# from standard input.
minuet = stdarray.create2D(11, 16, None)
for i in range(11):
    for j in range(16):
        minuet[i][j] = stdio.readInt()

# create a 2D list trio with dimension (9 , 16) and filling the array with trio measures.
trio = stdarray.create2D(6, 16, None)
for i in range(6):
    for j in range(16):
        trio[i][j] = stdio.readInt()

# standard output for random sequences of 16 minuet measures.
for b in range(16):
    # column index j to random integer generated between the value [0,15]
    j = stdrandom.uniformInt(0, 16)
    # random  number obtain from   die roll
    roll1 = stdrandom.uniformInt(0, 6)
    roll2 = stdrandom.uniformInt(0, 6)
    # row index is set set to sum of two die roll.
    i = roll1 + roll2
    stdio.write(str(minuet[i][j]) + ' ')

# standard output for random sequences of 16 trio measures.
for b in range(16):
    # column index  j is random integer value between [0,15] and row index i is the random
    # integer value between [0, 5]
    j = stdrandom.uniformInt(0, 16)
    i = stdrandom.uniformInt(0, 6)
    stdio.write(str(trio[i][j]) + ' ')
# new line at the end
stdio.writeln()
