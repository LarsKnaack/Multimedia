import operator

from Aufgabe1.Node import Node


class HuffmanCode:
    def __init__(self):
        self.letters = 0
        self.chars = {}

    def readfile(self, filename):
        f = open(filename, 'r')

        for line in f:
            for char in line:
                if char not in self.chars.keys():
                    self.chars[char] = 1
                else:
                    self.chars[char] += 1

                self.letters += 1

        f.close()

        self.chars = self.sortDict(self.chars)

    @staticmethod
    def create_tree(dictionary):
        nodes = []

        for key, value in dictionary.items():
            n = Node(key, value)
            nodes.append(n)

        nodes = sorted(nodes, key=operator.attrgetter('v'))
        counter = 0
        while 1 < len(nodes):
            n0 = nodes.pop(0)
            n1 = nodes.pop(0)

            new = Node("root" + str(counter), n0.v + n1.v)
            new.l = n0
            new.r = n1
            nodes.append(new)
            nodes = sorted(nodes, key=operator.attrgetter('v'))
            counter += 1

        return nodes[0]

    def coding_text(self, readfile, writefile):

        readf = open(readfile, 'r')
        writef = open(writefile, 'w')

        for line in readf:
            for char in line:
                writef.write(self.codes[char])

        writef.close()
        readf.close()
