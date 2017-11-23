from util import *
from int_util import *
from preprocessing import *
import bitstring

def hash_256(message):

    #preprocessing
    bin_message = pad(message)
    block_list = parse(bin_message)

    sha = init_hash_values

    #main loop
    for i in range(len(block_list)):

        reg = init_registers()

        print_reg(reg)

        for j in range(0,63):

            CH = ch(reg['e'],reg['f'],reg['g'])
            MAJ = maj(reg['a'],reg['b'],reg['c'])

            sig0 = sig_0(reg['a'])
            sig1 = sig_1(reg['e'])

            w_list = expand_blocks(block_list[0])

            T1 = reg['h'] + sig1 + CH + k_values[j] + w_list[j]
            T2 = sig0 + MAJ

            reg['h'] = reg['g']
            reg['g'] = reg['f']
            reg['e'] = (reg['d'] + T1) % (1<<32)
            reg['d'] = reg['c']
            reg['c'] = reg['b']
            reg['b'] = reg['a']
            reg['a'] = (T1 + T2) % (1<<32)

            print_reg(reg)

        #update intermediate hash values
        sha[0] = sha[0] + reg['a']
        sha[1] = sha[1] + reg['b']
        sha[2] = sha[2] + reg['c']
        sha[3] = sha[3] + reg['d']
        sha[4] = sha[4] + reg['e']
        sha[5] = sha[5] + reg['f']
        sha[6] = sha[6] + reg['g']
        sha[7] = sha[7] + reg['h']


    return [hex(i) for i in sha]

def init_registers():

    reg = dict()
    reg['a'] = init_hash_values[0]
    reg['b'] = init_hash_values[1]
    reg['c'] = init_hash_values[2]
    reg['d'] = init_hash_values[3]
    reg['e'] = init_hash_values[4]
    reg['f'] = init_hash_values[5]
    reg['g'] = init_hash_values[6]
    reg['h'] = init_hash_values[7]
    return reg


def expand_blocks(block):

    w_list = []

    for j in range(0,16):
        chunk = block[j*32:(j+1)*32]
        w = bitstring.BitArray(chunk).uint
        w_list.append(w)


    for j in range(16,64):

        t1 = sub_1(w_list[j-2])
        t2 = w_list[j-7]
        t3 = sub_0(w_list[j-15])
        t4 = w_list[j-16]

        w = (t1+t2+t3+t4) % (1<<32)

        w_list.append(w)

    return w_list


def print_reg(reg):
    hex_list = []
    for k, v in reg.items():
        hex_list.append(hex(v))
    print(hex_list)

print(hash_256("abc"))
