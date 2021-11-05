import stdaudio
import stdio
import sys

# read all remaining tokens and return them as an array of integers.
waltz = stdio.readAllInts()

# if the length of the array is not equals to 32
# exit with the message "A waltz must contain exactly 32 measures".
if len(waltz) != 32:
    sys.exit("A waltz must contain exactly 32 measures")

# if the elements between array 0 to 15 of waltz is greater than 176 or less than 1
# exit with the message "A minuet measure must be from [1, 176]"
for i in range(16):
    if (waltz[i] < 1) or (waltz[i] > 176):
        sys.exit("A minuet measure must be from [1, 176]")

# if the elements between array 16 to 31 of waltz is greater than 96 or less than 1
# exit with the message "A trio measure must be from [1, 176]"
for i in range(16, 31):
    if (waltz[i] < 1) or (waltz[i] > 96):
        sys.exit("A trio measure must be from [1, 96]")

# if there is no input error , play the first 16 minuet measures by calling stdio.playFile() with
# corresponding minuet filename.

for i in range(16):
    stdaudio.playFile('data/M' + str(waltz[i]))
#  play the last 16 trio   measures by calling stdio.playFile() with corresponding trio filename.
for i in range(16, 31):
    stdaudio.playFile('data/T' + str(waltz[i]))
stdio.writeln()
