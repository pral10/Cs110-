import math
import stdio


# Entry point.
def main():
    # initialize ETA, RHO, T, and R to appropriate values
    ETA = 9.135E-4
    RHO = 0.5E-6
    T = 297
    R = 8.31457

    #  Calculate var as the sum of the squares of the n displacements (each converted from
    # pixels to meters) read from standard input
    n = 0
    var = 0
    while not stdio.isEmpty():
        r = stdio.readFloat()
        converted_r = r * 0.175E-6
        squared_r = converted_r ** 2
        var += squared_r
        n += 1

    #  Divide var by 2 * n
    var = var / (2 * n)

    #  Estimate Boltzmann’s constant as 6 * math.pi * var * ETA * RHO / T
    boltzconst = 6 * math.pi * var * ETA * RHO / T

    #  Estimate Avogadro’s constant as R / k
    Avogardoconst = R / boltzconst

    #  Write to standard output the two constants in scientific notation (using the format
    # string ’%e’) and separated by a space

    stdio.writef('%e %e\n', boltzconst, Avogardoconst)


if __name__ == '__main__':
    main()
