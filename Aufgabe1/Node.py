class Node:
    def __init__(self, key, val):
        self.l = None
        self.r = None
        self.k = key
        self.v = val

    def generate_codes(self):
        codes = {}
        self.get_code_recursive(self.l, "0", codes)
        self.get_code_recursive(self.r, "1", codes)
        return codes

    def get_code_recursive(self, root, code, codes):
        if root.l is not None and root.r is not None:
            self.get_code_recursive(root.l, code + "0", codes)
            self.get_code_recursive(root.r, code + "1", codes)

        else:
            codes[root.k] = code
