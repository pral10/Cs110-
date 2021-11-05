import stdio
import rsa
import sys


def main():
    # Accept lo (int) and hi (int) as command-line arguments
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    # Get public/private keys as a tuple
    n, e, d = rsa.keygen(lo, hi)
    # Write the three values in the tuple, separated by a space
    stdio.writeln(str(n) + ' ' + str(e) + ' ' + str(d))


if __name__ == '__main__':
    main()
