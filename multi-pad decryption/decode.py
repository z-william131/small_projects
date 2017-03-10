import string

# xor two ASCII strings
def strxor(a, b):
    return bytes(x ^ y for (x, y) in zip(a, b))

# The main function: input one is a list of ciphertexts, input two is the target we are going to decode.

def decode_accurate(ciphertexts, target):

    spaces = {}
    for i in range(len(ciphertexts)):
        spaces[i] = []

    ciphers = ciphertexts[:]
    ciphers.append(target)

    # Find the each sentences' space position.
    for i in range(0, 10):
        space_count = {}
        for j in range(0,10):
            if i != j:
                result = strxor(bytes.fromhex(ciphers[i]), bytes.fromhex(ciphers[j]))
                index = 0
                for r in result:
                    if chr(r) in string.printable and chr(r).isalpha():
                        if index in space_count:
                            space_count[index] += 1
                        else:
                            space_count[index] = 1
                    index += 1
        for key, value in space_count.items():
            if value > 7:
                spaces[i].append(key)

    # Construct the decode answer

    answer = ["_"] * (len(Target) //2)

    for i in range(0, 9):
        result = strxor(bytes.fromhex(ciphers[i]), bytes.fromhex(Target))
    for index in spaces[i]:
        answer[index] = chr(result[index])

    final = ""
    for a in answer:
        final += a

    return final


def decode_rough(ciphertexts, target):

    answer = ["_"] * (len(Target) //2)

    for cipher in ciphers:
        results += [strxor(bytes.fromhex(cipher), bytes.fromhex(Target))]

    for result in results:
        index = 0
        for letter in result:
            if (letter >= 65 and letter <= 90) or letter == 32:
                answer[index] = chr(letter)
            index += 1

    final = ""
    for a in answer:
        final += a

    return final

