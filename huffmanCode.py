import operator
import collections

class Node:
    def __init__(self, key, val):
        self.l = None
        self.r = None
        self.k = key
        self.v = val
        self.c = ""

    def getCode(self, codes):
    	self.getCodeR(self.l, "0", codes)
    	self.getCodeR(self.r, "1", codes)


    def getCodeR(self, root, code, codes):
    	if root.l != None and root.r != None:
    		self.getCodeR(root.l, code + "0", codes)
    		self.getCodeR(root.r, code + "1", codes)

    	else:
    		#print("Key: " + root.k + " Code: " + code)
    		codes[root.k] = code

class HuffmanCode():

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

	def sortDict(self, dict):

		chars = collections.OrderedDict()
		for (key, value) in sorted(dict.items(), key = operator.itemgetter(1), reverse = True):
			chars[key] = value
		
		return chars

	def mergeValues(self):

		chars = self.chars.copy()

		counter = 0
		nodes = []

		for key, value in chars.items():
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
#			for node in nodes:
#				print("Node{Key: " + node.k + " Value: " + str(node.v))
#			print ("------------------------------------------------------------------")	

#		print(counter)

		self.tree = nodes[0]

	def generateCode(self):

		codes = {}
		self.tree.getCode(codes)
		print (codes)

		#print(self.chars)
		#print(len(self.chars))
		summe = 0
		for key, value in self.chars.items():
			for char, code in codes.items():
				if char == key:
					summe += value * len(code)

		print(float(summe)/ self.letters)
		print(7)

		self.codes = codes

	def codingText(self, readfile, writefile):

		readf = open(readfile, 'r')
		writef = open(writefile, 'w')

		for line in readf:
			for char in line:
				writef.write(self.codes[char])

		writef.close()
		readf.close()


if __name__ == "__main__":

	a = HuffmanCode()

	a.readfile("midsummer.txt")
	a.mergeValues()
	a.generateCode()
	a.codingText("midsummer.txt", "binarycode.txt")
