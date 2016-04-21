import collections
import operator

import math

from HuffmanCode import HuffmanCode


def sort_dict(dictionary):
    result = collections.OrderedDict()
    for (key, value) in sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True):
        result[key] = value

    return result


def readfile(filename):
    chars = {}
    letters = 0
    f = open(filename, 'r')

    for line in f:
        for char in line:
            if char not in chars.keys():
                chars[char] = 1
            else:
                chars[char] += 1

            letters += 1

    f.close()
    return letters, sort_dict(chars)

def coding_text(input_file, output_file, dictionary):

    readf = open(input_file, 'r')
    writef = open(output_file, 'w')

        for line in readf:
            for char in line:
                writef.write(dictionary[char])

        writef.close()
        readf.close()

if __name__ == "__main__":
    number_of_letters, character_dictionary = readfile("midsummer.txt")
    tree = HuffmanCode().create_tree(character_dictionary)
    code_dictionary = tree.generate_codes()
    print("Generated Huffman Codes:")
    print("%-10s %-10s %s" % ("Frequency", "Character", "Code"))
    average_huffman_length = 0.0
    for character, frequency in (sort_dict(character_dictionary)).items():
        code = code_dictionary.get(character)
        average_huffman_length += frequency * len(code)
        print("%-10d %-10s %s" % (frequency, repr(character), code))

    print("Average codelength in balanced binary tree:")
    print(math.log(len(character_dictionary), 2))
    print("Average codelength with huffmann coding:")
    print(average_huffman_length / number_of_letters)
