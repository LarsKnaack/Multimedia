import collections
import operator

import math

from Aufgabe1.HuffmanCode import HuffmanCode


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
