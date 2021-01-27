# ***************************************************
# Delaware State University
# Division of Physics, Engineering, Mathematics, and
# Computer Science
# CSCI-121 Elements of Computer Programming II
# Recitation 2 - Input/Output and Crypto
# ***************************************************

def crypto(filename, cypher):
    with open(filename, 'r') as fh, open(filename+'.enc', 'w') as fh_enc:
        for line in fh:
            e_line = ''
        for ch in line:
            e_line += cypher(ch)
        fh_enc.write(e_line)

# DO NOT touch the lines below
if __name__ == "__main__":
    crypto('hello.txt', lambda x: chr((ord(x) + 5) % 256))
