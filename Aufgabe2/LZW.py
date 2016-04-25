def encode(string):
    ascii_string = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    dictionary = {}
    for c in ascii_string:
        dictionary[c] = ord(c)
    last = ''
    code = ""

    index = 256
    for char in string:
        if str((last + char)) in dictionary.keys():
            last = last + char
        else:
            dictionary[str(last + char)] = index
            index += 1
            code += str(dictionary[last]) + "-"
            last = char
    code += str(dictionary[last]) + "-"
    return code[:-1]


def decode(string):
    ascii_string = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    dictionary = {}
    for c in ascii_string:
        dictionary[ord(c)] = c
    decoded_string = ""
    index = 256
    string = string.split("-")

    decoded_string += dictionary[int(string[0])]
    last = dictionary[int(string[0])]

    for char in string[1:]:
        current = dictionary[int(char)]
        decoded_string += current
        dictionary[index] = last + current[0]
        last = current
        index += 1

    return decoded_string


if __name__ == "__main__":
    test_string = "rabarbarbarbara"
    encoded = encode(test_string)
    decoded = decode(encoded)

    format_string = "%-15s %-35s %-15s"
    print(format_string % ("Test String", "Encoded", "Decoded"))
    print(format_string % (test_string, encoded, decoded))
    print(test_string == decoded)
