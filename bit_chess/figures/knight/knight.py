from bit_chess.utils import print_chess_mask, _64_bits_result


@_64_bits_result
def calculate_knight_step_mask(start_position):
    if start_position > 63:
        raise Exception('Figure position have to be in range [0..63]')

    figure_mask = 1 << start_position

    without_a = figure_mask & 0xfefefefefefefefe
    without_b = figure_mask & 0xfdfdfdfdfdfdfdfd
    without_ab = without_a & without_b

    without_g = figure_mask & 0xbfbfbfbfbfbfbfbf
    without_h = figure_mask & 0x7f7f7f7f7f7f7f7f
    without_gh = without_g & without_h

    step_mask = (without_a << 15) | (without_h << 17) | \
                (without_ab << 6) | (without_gh << 10) | \
                (without_ab >> 10) | (without_gh >> 6) | \
                (without_a >> 17) | (without_h >> 15)

    return step_mask


if __name__ == '__main__':
    mask = calculate_knight_step_mask(31)
    print_chess_mask(mask)
