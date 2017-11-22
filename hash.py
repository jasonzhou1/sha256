
#Main loop
def hash_256(block_list):

    for i in range(len(block_list)):

        '''
        Initialize registersa; b; c; d; e; f ; g; hwith the (i1)stintermediate
        hash value (=the initial hash value when i= 1)
        '''

        '''Apply theSHA-256 compression function to update registers'''