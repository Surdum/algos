import os
import io
import typing
from base import AlgoBase
from compression.utils import *
from queue import PriorityQueue
from collections import defaultdict


class Node:
    left: "Node" = None
    right: "Node" = None
    value: bytes
    count: int
    bit: bool

    def __init__(self, count: int, value: bytes):
        self.count = count
        self.value = value

    def __str__(self):
        return f"({self.count} {self.value})"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return Node(self.count + other.count, self.value + other.value)


class Huffman(AlgoBase):
    COMPRESS = 'compress'
    UNCOMPRESS = 'uncompress'

    def run(self, input_filename, output_filename, mode=COMPRESS):
        file = open(input_filename, 'rb')
        if mode == self.COMPRESS:
            _bytes = self._compress(file)
        elif mode == self.UNCOMPRESS:
            _bytes = self._decompress(file)
        else:
            raise
        with open(output_filename, 'wb') as f:
            f.write(_bytes)

    def compress_text(self, text):
        if isinstance(text, str):
            text = text.encode()
        return self._compress(io.BytesIO(text))

    def decompress_text(self, signs, text, source_file_size):
        if isinstance(text, str):
            text = text.encode()
        return self._decompress(signs, io.BytesIO(text), source_file_size)

    def _compress(self, _bytes):
        b = _bytes.read(1)
        freq_dict = defaultdict(int)
        while b:
            freq_dict[b] += 1
            b = _bytes.read(1)
        _bytes.seek(0)
        q = PriorityQueue()
        signs = set()
        for i in range(256):
            count = freq_dict.get(int_to_byte(i), 0)
            if count:
                signs.add(int_to_byte(i))
                q.put([count, int_to_byte(i)])
        values = []
        while not q.empty():
            elem = q.get()
            values.append(Node(*elem))
        while len(values) > 1:
            start_ids = []  # айдишники начал цепочек одинаковых элементов
            count = 0
            el = values[0]
            for i, elem in enumerate(values):
                if elem.count != el.count:
                    start_ids.append((i - 1, count))
                    el = elem
                    count = 1
                else:
                    count += 1
            if start_ids:
                start_ids.append((len(values) - 1, len(values) - 1 - start_ids[-1][0]))
            else:
                start_ids.append((len(values) - 1, len(values)))
            if start_ids[0][1] > 1:
                left = values[start_ids[0][0] - 1]
                right = values[start_ids[0][0]]
            else:
                left = values[start_ids[0][0]]
                right = values[start_ids[1][0]]
            new_node = left + right
            new_node.left = left
            new_node.right = right
            values.insert(0, new_node)
            values.remove(left)
            values.remove(right)
            values = sorted(values, key=lambda x: x.count)
        parent = values[0]
        b = _bytes.read(1)
        buffer = ''
        compressed = b''
        while b:
            buffer += self.get_code(parent, b)
            while len(buffer) >= 8:
                compressed += int_to_byte(self.str_to_int(buffer[:8]))
                buffer = buffer[8:]
            b = _bytes.read(1)
        if buffer:
            compressed += int_to_byte(self.str_to_int(buffer[:len(buffer)].ljust(8, '0')))
        return parent, compressed

    def get_code(self, node, code, bit=''):
        if node.value == code:
            return bit
        if node.left and code in node.left.value:
            return bit + self.get_code(node.left, code, '0')
        if node.right and code in node.right.value:
            return bit + self.get_code(node.right, code, '1')

    @staticmethod
    def str_to_int(bits_str):
        eta = 0b0000000
        for i in range(len(bits_str) - 1, -1, -1):
            if bits_str[len(bits_str) - 1 - i] == '1':
                eta |= 0b1 << i
        return eta

    def _decompress(self, parent, _bytes, source_file_size):
        def read_bits(f):
            while True:
                b = f.read(1)
                if not b:
                    return ''
                n = ord(b)
                for i in range(7, -1, -1):
                    yield str(int(bool(n & (1 << i))))
        bit_reader = read_bits(_bytes)
        bit = next(bit_reader)
        uncompressed = b''
        found = False
        current = parent
        bits = []
        while bit:
            bits.append(bit)
            if not current.left and not current.right:
                uncompressed += current.value
                source_file_size -= 1
                found = True
            if found:
                found = False
                current = parent
                continue
            if bit == '0':
                current = current.left
            else:
                current = current.right
            try:
                bit = next(bit_reader)
            except:
                if source_file_size > 0:
                    uncompressed += current.value
                break
        return uncompressed


if __name__ == '__main__':
    generate_random_file('not-compressed.txt', 128)
    huffman = Huffman()
    source = b'abcdefghijklmnopqrstuvwxyz'
    # source = 'hello, world'
    huffman_code, comp = huffman.compress_text(source)
    print('source len:', len(source))
    print('compressed len:', len(comp))
    uncomp = huffman.decompress_text(huffman_code, comp, len(source))
    print('same', source == uncomp)
    print()





