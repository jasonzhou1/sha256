import bitstring


# util function definitions meant to work with ints rather than binary list representation

# Right rotation of a list of bits, by n bits
def ror(i, n_bits):
    n = bitstring.BitArray(uint=i, length=32)
    n.ror(n_bits)
    return n.uint


# Logical right shift
def r_shift(i, n_bits):
    n = bitstring.BitArray(uint=i, length=32)
    n >>= n_bits
    return n.uint


def ch(x, y, z): return (x & y) ^ (~x & z)


def maj(x, y, z): return (x & y) ^ (x & z) ^ (y & z)


def sig_0(x):
    s2 = ror(x, 2)
    s13 = ror(x, 13)
    s22 = ror(x, 22)

    return s2 ^ s13 ^ s22


def sig_1(x):
    s6 = ror(x, 6)
    s11 = ror(x, 11)
    s25 = ror(x, 25)

    return s6 ^ s11 ^ s25


def sub_0(x):
    s7 = ror(x, 7)
    s18 = ror(x, 18)
    r3 = r_shift(x, 3)

    return s7 ^ s18 ^ r3


def sub_1(x):
    s17 = ror(x, 17)
    s19 = ror(x, 19)
    r10 = r_shift(x, 10)

    return s17 ^ s19 ^ r10
