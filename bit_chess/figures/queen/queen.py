from bit_chess.utils import print_chess_mask, _64_bits_result
from bit_chess.figures.rook import calculate_rook_step_mask
from bit_chess.figures.bishop import calculate_bishop_step_mask


@_64_bits_result
def calculate_queen_step_mask(start_position):
    if start_position > 63:
        raise Exception('Figure position have to be in range [0..63]')

    rook_steps = calculate_rook_step_mask(start_position)
    bishop_steps = calculate_bishop_step_mask(start_position)
    return rook_steps | bishop_steps


if __name__ == '__main__':
    mask = calculate_queen_step_mask(14)
    print_chess_mask(mask)
