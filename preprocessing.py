from util import tobits
import bitstring

"""
Pads a string message into 512 bit chunks.
"""
def pad(message):

    bin_message = tobits(message)
    l = len(bin_message)
    k = find_k(bin_message)

    bin_message.append(1)
    for i in range(k): bin_message.append(0)

    #append 64 bit representation of l
    bin_string = bin(l)[2:].zfill(64)
    for digit in bin_string:
        bin_message.append(int(digit))

    assert len(bin_message) % 512 == 0

    n = bitstring.BitArray(bin_message)
    return bin_message


def parse(bin_message):
    size = 512
    block_list = [bin_message[i:i+size] for i in range(0,len(bin_message),size)]
    return block_list


def find_k(bit_list):

    m_length = len(bit_list)
    k = 0

    while ((m_length + 1 + k) % 512) != 448: k+=1
    return k

