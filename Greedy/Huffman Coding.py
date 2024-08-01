import heapq
from collections import Counter, defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = Counter(text)
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)
    
    return priority_queue[0]

def build_code_table(node, prefix='', code_table=defaultdict()):
    if node is not None:
        if node.char is not None:
            code_table[node.char] = prefix
        build_code_table(node.left, prefix + '0', code_table)
        build_code_table(node.right, prefix + '1', code_table)
    return code_table

def huffman_encoding(text):
    root = build_huffman_tree(text)
    code_table = build_code_table(root)
    encoded_text = ''.join(code_table[char] for char in text)
    return encoded_text, code_table

def huffman_decoding(encoded_text, code_table):
    reverse_code_table = {code: char for char, code in code_table.items()}
    decoded_text = []
    code = ''
    for bit in encoded_text:
        code += bit
        if code in reverse_code_table:
            decoded_text.append(reverse_code_table[code])
            code = ''
    return ''.join(decoded_text)

# Example usage
text = "this is an example for huffman encoding"
encoded_text, code_table = huffman_encoding(text)
print("Encoded text:", encoded_text)
print("Code table:", code_table)
decoded_text = huffman_decoding(encoded_text, code_table)
print("Decoded text:", decoded_text)
