#this entire module exists to compress a file and represent it in base 9
#and provide the inverse

#it's generalized

#note that the format of number base n is actually an array of base n digits
#in reverse order, because it's more convenient for me that way

#should totally make this an object that would make the most sense

from zlib import compress, decompress

maginum = 9 #there aren't constants in this goddamn language

#converts given val to the base specified by maginum
#represents as a list of digits from least-order to greatest-order
#e.g. 100 => [0, 0, 1]
def base_magi(val):
    #presumes val is base 10
    base_n = []
    
    while(val):
        base_n.append(val % maginum)
        val = int(val / maginum)

    return base_n

#converts a number base_n as represented by base_magi back into base 10
def base_ten(base_n):
    #presumes base_n is in base maginum
    val = 0
    
    for i in range(len(base_n)):
        val += (maginum ** i) * base_n[i]

    return val

#compresses a file and represents it as a series of base maginum integers
def alchemize(reagents):
    arcanum = compress(reagents.encode('utf-8'), maginum)

    return [base_magi(e) for e in list(arcanum)]

#takes a file processed by alchemize and decompresses it back to a normal file
def dealchemize(transmutation):
    arcanum = bytes([base_ten(e) for e in transmutation])

    return decompress(arcanum).decode('utf-8')

#gets the contents of a file f
def get_reagents(f):
    return open(f, 'r').read()

#get and set functions for maginum which are here for some reason
def get_maginum():
    return maginum

def set_maginum(newnum):
    global maginum
    maginum = newnum
