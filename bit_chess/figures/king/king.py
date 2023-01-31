from bit_chess.utils import print_chess_mask, _64_bits_result


@_64_bits_result
def calculate_king_step_mask(king_position: int):
    if king_position > 63:
        raise Exception('King position have to be in range [0..63]')

    king_mask = 1 << king_position
    without_a = king_mask & 0xfefefefefefefefe
    without_h = king_mask & 0x7f7f7f7f7f7f7f7f

    step_mask = (without_a << 7) | (king_mask << 8) | (without_h << 9) | \
                (without_a >> 1) | (without_h << 1) | \
                (without_a >> 9) | (king_mask >> 8) | (without_h >> 7)

    return step_mask


if __name__ == '__main__':
    mask = calculate_king_step_mask(60)
    print(mask)
    print_chess_mask(mask)
