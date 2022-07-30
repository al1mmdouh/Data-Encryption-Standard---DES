# import keyGen

arrPC1 = [[57, 49, 41, 33, 25, 17, 9], [1, 58, 50, 42, 34, 26, 18], [10, 2, 59, 51, 43, 35, 27], [19, 11, 3, 60, 52, 44, 36], [
    63, 55, 47, 39, 31, 23, 15], [7, 62, 54, 46, 38, 30, 22], [14, 6, 61, 53, 45, 37, 29], [21, 13, 5, 28, 20, 12, 4]]
arrPC2 = [[14, 17, 11, 24, 1, 5], [3, 28, 15, 6, 21, 10], [23, 19, 12, 4, 26, 8], [16, 7, 27, 20, 13, 2], [
    41, 52, 31, 37, 47, 55], [30, 40, 51, 45, 33, 48], [44, 49, 39, 56, 34, 53], [46, 42, 50, 36, 29, 32]]
arrIP = [[58, 50, 42, 34, 26, 18, 10, 2], [60, 52, 44, 36, 28, 20, 12, 4], [62, 54, 46, 38, 30, 22, 14, 6], [64, 56, 48, 40, 32, 24, 16, 8], [
    57, 49, 41, 33, 25, 17, 9, 1], [59, 51, 43, 35, 27, 19, 11, 3], [61, 53, 45, 37, 29, 21, 13, 5], [63, 55, 47, 39, 31, 23, 15, 7]]
arrESelection = [[32, 1, 2, 3, 4, 5], [4, 5, 6, 7, 8, 9], [8, 9, 10, 11, 12, 13], [12, 13, 14, 15, 16, 17], [
    16, 17, 18, 19, 20, 21], [20, 21, 22, 23, 24, 25], [24, 25, 26, 27, 28, 29], [28, 29, 30, 31, 32, 1]]
afterSBoxPermutation = [[14, 7, 20, 21], [29, 12, 28, 17], [1, 15, 23, 26], [
    5, 18, 31, 10], [2, 8, 24, 14], [32, 27, 3, 9], [19, 13, 30, 6], [22, 11, 4, 25]]
arrInversePermutation = [[40, 8, 48, 16, 56, 24, 64, 32], [39, 7, 47, 15, 55, 23, 63, 31], [38, 6, 46, 14, 54, 22, 62, 30], [37, 5, 45, 13, 53, 21, 61, 29], [
    36, 4, 44, 12, 52, 20, 60, 28], [35, 3, 43, 11, 51, 19, 59, 27], [34, 2, 42, 10, 50, 18, 58, 26], [33, 1, 41, 9, 49, 17, 57, 25]]
table = [
        ["0010", "1100", "0100", "0001", "0111", "1010", "1011", "0110", "1000", "0101", "0011", "1111", "1101", "0000", "1110", "1001"],
        ["1110", "1011", "0010", "1100", "0100", "0111", "1101", "0001", "0101", "0000", "1111", "1010", "0011", "1001", "1000", "0110"],
        ["0100", "0010", "0001", "1011", "1010", "1101", "0111", "1000", "1111", "1001", "1100", "0101", "0110", "0011", "0000", "1110"],
        ["1011", "1000", "1100", "0111", "0001", "1110", "0010", "1101", "0110", "1111", "0000", "1001", "1010", "0100", "0101", "0011"]
    ]
arrOfSteps = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def fill(variable, arr):
    key = ""
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            key += variable[arr[i][j] - 1]
    return key


def rotate(input, d):

    Lfirst = input[0: d]
    Lsecond = input[d:]
    # now concatenate two parts together
    return (Lsecond + Lfirst)


def offsetShifting(c_zero, d_zero):
    arrayOfCs = []
    arrayOfDs = []
    for i in range(len(arrOfSteps)):
        c_zero = rotate(c_zero, arrOfSteps[i])
        arrayOfCs.append(bin(int(c_zero, 2))[2:].zfill(28))
        print("C"+str(i+1)+": "+str(arrayOfCs[i]))
        d_zero = rotate(d_zero, arrOfSteps[i])
        arrayOfDs.append(bin(int(d_zero, 2))[2:].zfill(28))
        print("D"+str(i+1)+": "+str(arrayOfDs[i])+'\n')
    return arrayOfCs, arrayOfDs


def sBOx(xor_output):
    xor_output_splited = [xor_output[i:i+6]
                          for i in range(0, len(xor_output), 6)]
    
    sBoxOutput = ""
    for i in xor_output_splited:
        row = i[0] + i[-1]
        colomn = i[1:5]
        sBoxOutput += table[int(row, 2)][int(colomn, 2)]
    return sBoxOutput


# RHS[i],key[i] #steps: 1-expand RHS, 2- XOR new RHS with key[i], 3- sboxes
def manglerF(RHS, key,i):
    # print("RHS: "+RHS+" LEN: "+str(len(RHS)))  # always 32 bit first
    # print("Key: "+key+" LEN: "+str(len(key)))  # always 48 bit first
    # step1 : e selection
    RHS = fill(RHS, arrESelection)  # =48 bits after e selection
    print("NEW RHS after E selection: "+RHS+" len: "+str(len(RHS)))
    # step2 : xor new rhs with key
    xor_output = bin(int(key, 2) ^ int(RHS, 2))[2:].zfill(48)
    print("XOR Output: "+xor_output+" len: "+str(len(xor_output)))
    # step3 : s boxes
    sBoxOutput = sBOx(xor_output)
    print("S Box Output"+str(i)+": "+sBoxOutput)
    permutationOutput = fill(sBoxOutput, afterSBoxPermutation)
    return permutationOutput


def keyGeneration(quantity):

    hex_size = len(quantity)*4
    binQuantity = bin(int(quantity, 16))[2:].zfill(hex_size)
    print("Quantity with 8 bits: "+binQuantity+'\n')

    key = fill(binQuantity, arrPC1)
    print("Key after PC-1: "+key+'\n')

    c_zero = key[:28]
    d_zero = key[28:]

    print("C0: "+c_zero)
    print("D0: "+d_zero+'\n')

    arrayOfCs, arrayOfDs = offsetShifting(c_zero, d_zero)

    arrayOfKeys = []
    key = ""

    for i in range(len(arrayOfCs)):
        key += fill(arrayOfCs[i] + arrayOfDs[i], arrPC2)
        print("Key"+str(i)+": "+key)
        arrayOfKeys.append(key)
        key = ""
    print('\n')
    return arrayOfKeys


def encrypt(mText, arrayOfKeys):

    binMText = bin(int(mText, 16))[2:].zfill(64)
    print("Text: "+binMText+'\n')

    ipTxt = fill(binMText, arrIP)
    print("Text After IP: "+ipTxt+'\n')

    # print(len(ipTxt))

    RHS = ipTxt[32:]
    LHS = ipTxt[:32]

    print("Left Hand Side: "+LHS)
    print("Right Hand Side: "+RHS)

    for i in range(len(arrayOfKeys)):

        oldLeft = LHS
        LHS = RHS #new left = old right
        permutationOutput = manglerF(RHS, arrayOfKeys[i],i)
        RHS = bin(int(oldLeft, 2) ^ int(permutationOutput, 2) )[2:].zfill(32)
        print('\n'+"LHS"+str(i+1)+": "+LHS)
        print("RHS"+str(i+1)+": "+RHS)
        
    
    afterShuffle = (RHS+LHS)
    print("After Shuffle: "+afterShuffle+" len: "+str(len(afterShuffle)))

    finalOutput = fill(afterShuffle, arrInversePermutation)

    print("Cipher Text: " +
          finalOutput+" len: "+str(len(afterShuffle)))

    return finalOutput

def decrypt(cipherText,arrayOfKeys):

    ipTxt = fill(cipherText,arrIP)
    
    
    RHS = ipTxt[32:]
    LHS = ipTxt[:32]

    print("Left Hand Side: "+LHS)
    print("Right Hand Side: "+RHS)

    for i in reversed(range(len(arrayOfKeys))):

        oldLeft = LHS   
        LHS = RHS #new left = old right
        permutationOutput = manglerF(RHS, arrayOfKeys[i],i)
        RHS = bin(int(oldLeft, 2) ^ int(permutationOutput, 2) )[2:].zfill(32)
        print('\n'+"LHS"+str(i+1)+": "+LHS)
        print("RHS"+str(i+1)+": "+RHS)
        
    
    afterShuffle = (RHS+LHS)
    print("After Shuffle: "+afterShuffle+" len: "+str(len(afterShuffle)))

    finalOutput = fill(afterShuffle, arrInversePermutation)

    print("Plaintext: "+hex(int(finalOutput,2))[2:])


def run():
    with open("test.txt") as file:
        file = file.read()
        quantityArr = file.split('\n')
        quantity = quantityArr[0]
        mText = quantityArr[1]

    arrayOfKeys = keyGeneration(quantity)

    cipherText = encrypt(mText, arrayOfKeys)

    decrypt(cipherText,arrayOfKeys)


run()
