from bit_chess.utils import print_chess_mask, _64_bits_result


@_64_bits_result
def calculate_rook_step_mask(start_position):
    if start_position > 63:
        raise Exception('Figure position have to be in range [0..63]')

    figure_mask = 1 << start_position

    first_line = 0xff
    a_line = 0x101010101010101
    left_coord = start_position % 8
    bottom_coord = start_position // 8
    step_mask = ((a_line << left_coord) | (first_line << (bottom_coord * 8))) ^ figure_mask

    return step_mask


if __name__ == '__main__':
    mask = calculate_rook_step_mask(59)
    print_chess_mask(mask)
