import os
from random import randint


def generate_random_file(filename, size):
    with open(filename, 'wb') as f:
        for _ in range(size):
            f.write(int_to_bytes(randint(0, 255)))


def is_same_content(filename1, filename2):
    return open(filename1, 'rb').read() == open(filename2, 'rb').read()


def file_info(filename):
    size = os.path.getsize(filename)
    print(f'Name: {filename}\nSize: {size}')


def int_to_bytes(number: int, signed=False) -> bytes:
    return number.to_bytes(length=(8 + (number + (number < 0)).bit_length()) // 8, byteorder='big', signed=signed)


def int_from_bytes(binary_data: bytes, signed=False) -> int:
    return int.from_bytes(binary_data, byteorder='big', signed=signed)

