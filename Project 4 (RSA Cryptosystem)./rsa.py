import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    # get a list of primes between interval[lo,hi]
    prime1 = _primes(lo, hi)

    # sample two distinct primes form the list prime1
    p, q = _sample(prime1, 2)

    # set n and m to pq and (p-1)(q-1) respectively
    n = p*q
    m = (p-1)*(q-1)

    # get a list prime from interval [2,m)
    prime2 = _primes(2, m)

    # Choosing a random prime e from the list such that e does not divide m.
    e = _choice(prime2)
    while m % e == 0:
        e = _choice(prime2)

    # Find a d ∈ [1, m) such that ed mod m is equal to  1
    d = stdrandom.uniformInt(1, m)
    while (e*d) % m != 1:
        d = stdrandom.uniformInt(1, m)

    # return tuple(n, e, d)
    return n, e, d


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    enc = (x**e) % n
    return enc


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    dec = (y**d) % n
    return dec


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % width)


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    prime = []
    for p in range(lo, hi+1):
        if p > 1:
            for j in range(2, p):
                if p % j == 0:
                    break
            else:
                prime += [p]

    return prime


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    b = a[:]
    for i in range(k):
        rand_index = stdrandom.uniformInt(0, len(b))
        temp = b[i]
        b[i] = b[rand_index]
        b[rand_index] = temp

    return b[:k]


# Returns a random item from the list a.
def _choice(a):
    r = stdrandom.uniformInt(0, len(a))
    return a[r]


# Unit tests the library [DO NOT EDIT].
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()
