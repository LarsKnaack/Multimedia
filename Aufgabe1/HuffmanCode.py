import operator

from Node import Node


class HuffmanCode:

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
