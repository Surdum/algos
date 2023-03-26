import os
from base import AlgoBase
from compression.utils import *


class RLE(AlgoBase):
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

    def _compress(self, file):
        sign = file.read(1)
        number = 1
        compressed = b''
        while True:
            b = file.read(1)
            if not b:
                break
            if b == sign:
                number += 1
            else:
                compressed += bytes([number]) + sign
                sign = b
                number = 1
            if number == 255:
                compressed += bytes([number]) + sign
                number = 0
        compressed += bytes([number]) + sign
        return compressed

    def _decompress(self, file):
        decompressed = b''
        while True:
            number = int_from_bytes(file.read(1))
            if not number:
                break
            sign = file.read(1)
            for _ in range(number):
                decompressed += sign
        return decompressed


class BetterRLE(AlgoBase):
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

    def _compress(self, file):
        sign = file.read(1)
        number = 1
        compressed = b''
        alone_stack = []
        while True:
            b = file.read(1)
            if not b:
                break
            if b == sign:
                number += 1
                if number > 1 and alone_stack:
                    compressed += int_to_bytes(-len(alone_stack), signed=True)
                    while alone_stack:
                        compressed += alone_stack.pop(0)
            elif b != sign and number == 1:
                alone_stack.append(sign)
                sign = b
                number = 1
            else:
                compressed += int_to_bytes(number, signed=True) + sign
                number = 1
                sign = b
            if number == 127:
                compressed += int_to_bytes(number, signed=True) + sign
                number = 0
            if len(alone_stack) == 127:
                compressed += int_to_bytes(-len(alone_stack), signed=True)
                while alone_stack:
                    compressed += alone_stack.pop(0)
        if alone_stack:
            compressed += int_to_bytes(-len(alone_stack), signed=True)
            while alone_stack:
                compressed += alone_stack.pop(0)
        compressed += int_to_bytes(number, signed=True) + sign
        return compressed

    def _decompress(self, file):
        decompressed = b''
        while True:
            number = int_from_bytes(file.read(1), signed=True)
            if not number:
                break
            if number < 0:
                for _ in range(abs(number)):
                    decompressed += file.read(1)
            else:
                b = file.read(1)
                for _ in range(number):
                    decompressed += b
        return decompressed


if __name__ == '__main__':
    # generate_random_file('not-compressed.txt', 2048)
    rle = RLE()
    print('RLE')
    file_info('not-compressed.txt')
    rle.run('not-compressed.txt', 'compressed.txt')
    file_info('compressed.txt')
    rle.run('compressed.txt', 'uncompressed.txt', mode=RLE.UNCOMPRESS)
    file_info('uncompressed.txt')
    print('Is same:', is_same_content('not-compressed.txt', 'uncompressed.txt'))
    print()

    brle = BetterRLE()
    print('RLE Optimized')
    file_info('not-compressed.txt')
    brle.run('not-compressed.txt', 'compressed-b.txt')
    file_info('compressed-b.txt')
    brle.run('compressed-b.txt', 'uncompressed-b.txt', mode=RLE.UNCOMPRESS)
    file_info('uncompressed-b.txt')
    print('Is same:', is_same_content('not-compressed.txt', 'uncompressed-b.txt'))
