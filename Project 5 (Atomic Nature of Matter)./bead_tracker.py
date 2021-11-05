import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    #  Accept command-line arguments pixels (int), tau (float), and delta (float)
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])

    #  Construct a BlobFinder object for the frame sys.argv[4] and from it get a list of beads
    pict = Picture(sys.argv[4])
    bf1 = BlobFinder(pict, tau)

    # prevBeads that have at least pixels
    #  For each frame starting at sys.argv[5]:
    prevBeads = bf1.getBeads(pixels)

    # This test start from the argv[5]
    for v in sys.argv[5:]:
        #  Construct a BlobFinder object
        pic2 = Picture(v)
        bf2 = BlobFinder(pic2, tau)

        #  and from it get a list of beads currBeads that have at least pixels pixels
        curBeads = bf2.getBeads(pixels)

        #  For each bead curBead in curBeads,
        for currBead in curBeads:
            min_distance = math.inf

            # find a bead prevBead from prevBeads that is no further
            for prevBead in prevBeads:
                if currBead.distanceTo(prevBead) < min_distance:
                    min_distance = currBead.distanceTo(prevBead)

                # than delta and is closest to currBead, and if such a bead is found, write
                # its distance
                # (using format string ’%.4f\n’) to currBead
            if min_distance <= delta:
                # (using format string ’%.4f\n’) to currBead
                stdio.writef('%.4f\n', min_distance)

        #  Write a newline character
        stdio.write('\n')
        # Set prevBeads to currBead
        prevBeads = curBeads


if __name__ == '__main__':
    main()
