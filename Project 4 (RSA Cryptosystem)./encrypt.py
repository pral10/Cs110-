import rsa
import stdio
import sys


# Entry point.
def main():
    # Accept public-key n (int) and e (int) as command-line arguments
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    # Get the number of bits per character (called it width).
    width = rsa.bitLength(n)

    # Accepted message to encrypt from standard input
    msg = stdio.readAll()

    # For each character c in message
    for c in msg:
        # Used the built-in function ord() to turn c into an integer x
        x = ord(c)
        # Encrypt x
        x = rsa.encrypt(x, n, e)
        # Write the encrypted value as a width-long binary string
        stdio.write(rsa.dec2bin(x, width))
    # Write a newline character
    stdio.writeln()


if __name__ == '__main__':
    main()
