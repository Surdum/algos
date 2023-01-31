import os


def print_chess_mask(mask: int):
    bits = bin(mask)[2:].rjust(64, '0')
    lines = []
    line = []
    for i, elem in enumerate(bits):
        i += 1
        line.append(elem)
        if i % 8 == 0:
            lines.append(line[::-1])
            line = []

    for line in lines:
        print('  '.join(line))


def cut_left_bits(number, bit_len=64):
    """
    Cuts everything after 'bin_len' bit
    :param number: target number
    :param bit_len: length in bits of the result
    :return:
    """
    return int(bin(number)[2:][-bit_len:], 2)


def _64_bits_result(func):
    """
    Make function result 64-bit length
    :param func:
    :return:
    """
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return cut_left_bits(result, bit_len=64)
    return inner


def count_non_zero_bits_1(number):
    c = 0
    while number > 0:
        if number & 1 == 1:
            c += 1
        number >>= 1
    return c


def count_non_zero_bits_2(number):
    c = 0
    while number > 0:
        number = number & (number - 1)
        c += 1
    return c


def load_input_data(*path):
    return int(open(os.path.join(*path)).read().strip())


def load_output_data(*path: str):
    bit_count, mask = open(os.path.join(*path)).read().strip().split('\n')
    return int(bit_count), int(mask)


if __name__ == '__main__':
    # print_chess_mask(1)
    # print(cut_left_bits(18446744073709551618))
    print(count_non_zero_bits_1(110333))
    print(count_non_zero_bits_2(110333))
