import os
from random import randint


def generate_random_file(filename, size):
    with open(filename, 'wb') as f:
        for _ in range(size):
            f.write(int_to_bytes(randint(0, 255)))


def file_content_is_same(fp1, fp2):
    try:
        with open(fp1, 'rb') as f1, open(fp2, 'rb') as f2:
            if f1.read(1) != f2.read(1):
                return False
    except StopIteration:
        return False
    return True


def file_info(filename):
    size = os.path.getsize(filename)
    print(f'Name: {filename}\nSize: {size}')


def int_to_bytes(number: int, signed=False) -> bytes:
    return number.to_bytes(length=(8 + (number + (number < 0)).bit_length()) // 8, byteorder='big', signed=signed)


def int_from_bytes(binary_data: bytes, signed=False) -> int:
    return int.from_bytes(binary_data, byteorder='big', signed=signed)

