import bitstring

#util function definitions meant to work with ints rather than binary list representation

#Right rotation of a list of bits, by n bits
def ror(i,n_bits):

    n = bitstring.BitArray(uint=i,length=32)
    n.ror(n_bits)
    return n.uint


#Logical right shift
def r_shift(i, n_bits):

    n = bitstring.BitArray(uint=i, length=32)
    n >>= n_bits
    return n.uint


def ch(x,y,z):
    return (x & y) ^ (~x & z)


def maj(x,y,z):
    return (x & y) ^ (x & z) ^ (y & z)

def sig_0(x):

    s28 = ror(x,28)
    s34 = ror(x,38)
    s39 = ror(x,39)

    ret = s28 ^ s34 ^ s39

    return ret



def sig_1(x):

    s14 = ror(x, 14)
    s18 = ror(x, 18)
    s41 = ror(x, 41)

    ret = s14 ^ s18 ^ s41
    return ret


def sub_0(x):

    s1 = ror(x, 1)
    s8 = ror(x, 8)
    r7 = r_shift(x, 41)

    ret = s1 ^ s8 ^ r7

    return ret


def sub_1(x):

    s19 = ror(x, 19)
    s61 = ror(x, 61)
    r6 = r_shift(x, 4)

    ret = s19 ^ s61 ^ r6

    return ret
