from util import *
from int_util import *
from preprocessing import *
import bitstring
import copy

def hash_256(message):

    #Preprocessing
    bin_message = pad(message)
    block_list = parse(bin_message)
    sha = copy.deepcopy(init_hash_values)

    #Main loop
    for i in range(len(block_list)):

        reg = update_registers(sha)

        w_list = expand_blocks(block_list[i])

        # print_reg(reg)

        for j in range(0,64):

            CH = ch(reg['e'],reg['f'],reg['g'])
            MAJ = maj(reg['a'],reg['b'],reg['c'])
            sig0 = sig_0(reg['a'])
            sig1 = sig_1(reg['e'])

            Wj_Kj = ( k_values[j] + w_list[j] )  % (1 << 32)
            t1_temp = (reg['h'] + Wj_Kj + CH ) % (1 << 32)
            T1 = ( t1_temp + sig1 ) % (1 << 32)

            T2 = (sig0 + MAJ) % (1 << 32)

            reg['h'] = reg['g']
            reg['g'] = reg['f']
            reg['f'] = reg['e']
            reg['e'] = (reg['d'] + T1) % (1<<32)
            reg['d'] = reg['c']
            reg['c'] = reg['b']
            reg['b'] = reg['a']
            reg['a'] = (T1 + T2) % (1<<32)

            # print_reg(reg)


        #update intermediate hash values
        sha[0] = (sha[0] + reg['a']) % (1<<32)
        sha[1] = (sha[1] + reg['b']) % (1<<32)
        sha[2] = (sha[2] + reg['c']) % (1<<32)
        sha[3] = (sha[3] + reg['d']) % (1<<32)
        sha[4] = (sha[4] + reg['e']) % (1<<32)
        sha[5] = (sha[5] + reg['f']) % (1<<32)
        sha[6] = (sha[6] + reg['g']) % (1<<32)
        sha[7] = (sha[7] + reg['h']) % (1<<32)

        # print([hex(i) for i in sha])

    return make_digest(sha)


def make_digest(sha):

    hash = ""

    for h in sha:
        hash+= hex(h)[2:]

    return hash

def update_registers(sha):

    reg = dict()
    reg['a'] = sha[0]
    reg['b'] = sha[1]
    reg['c'] = sha[2]
    reg['d'] = sha[3]
    reg['e'] = sha[4]
    reg['f'] = sha[5]
    reg['g'] = sha[6]
    reg['h'] = sha[7]
    return reg

def expand_blocks(block):

    w_list = [0]*64

    for j in range(0,16):
        chunk = block[j*32:(j+1)*32]
        w = bitstring.BitArray(chunk).uint
        w_list[j] = (w)

    for j in range(16,64):
        t1 = (sub_0(w_list[j-15]) + w_list[j-16]) % (1<<32)
        t2 = ( t1 + w_list[j-7] ) % (1<<32)
        t3 = ( t2 + sub_1(w_list[j-2])) % (1<<32)

        w_list[j] = t3

    return w_list


def print_reg(reg):
    hex_list = []
    for k, v in reg.items():
        hex_list.append(hex(v))
    print(hex_list)


x=hash_256("abc")
print(x)

y=hash_256("abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq")
print(y)


