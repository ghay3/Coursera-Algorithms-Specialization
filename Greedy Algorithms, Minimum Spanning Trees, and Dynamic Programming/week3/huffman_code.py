from queue import PriorityQueue


class Node:
    def __init__(self, symbol=None, left=None, right=None):
        self.symbol = symbol
        self.left = left
        self.right = right

    def __gt__(self, other):
        """ugly to make it enable to be used in pq from std"""
        return 0


class HuffmanCode:

    def __init__(self, symbol2freq):
        self.root = self.build_tree(symbol2freq)
        self.symbol2bits, self.bits2symbol = self.get_mapping(self.root)
        self.expected_len = self.compute_length(self.symbol2bits, symbol2freq)

    @staticmethod
    def build_tree(symbol2freq):
        pq = PriorityQueue()
        for symbol, freq in symbol2freq.items():
            pq.put((freq, Node(symbol=symbol)))
        while pq.qsize() > 1:
            freq1, node1 = pq.get()
            freq2, node2 = pq.get()
            pq.put((freq1 + freq2, Node(symbol=None, left=node1, right=node2)))
        return pq.get()[1]

    @staticmethod
    def get_mapping(root):
        symbol2bits, bits2symbol = {}, {}

        def traverse(node, bits):
            if node.symbol is not None:
                symbol2bits[node.symbol] = bits
                bits2symbol[bits] = node.symbol
            else:
                traverse(node.left, bits + '0')
                traverse(node.right, bits + '1')

        traverse(root, '')
        return symbol2bits, bits2symbol

    @staticmethod
    def compute_length(symbol2bits, symbol2freq):
        expected_len = 0
        all_freq = sum(symbol2freq.values())
        for symbol, bits in symbol2bits.items():
            expected_len += len(bits) * symbol2freq[symbol] / all_freq
        return expected_len


if __name__ == '__main__':
    # https://en.wikipedia.org/wiki/File:HuffmanCodeAlg.png
    symbol2freq = {
        'a': 15,
        'b': 7,
        'c': 6,
        'd': 6,
        'e': 5
    }
    hfc = HuffmanCode(symbol2freq)
    print(hfc.symbol2bits)
    print(hfc.expected_len)
