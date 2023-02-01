from bit_chess.utils import print_chess_mask, _64_bits_result


@_64_bits_result
def calculate_bishop_step_mask(start_position):
    if start_position > 63:
        raise Exception('Figure position have to be in range [0..63]')

    figure_mask = 1 << start_position

    main_diagonal = 0x8040201008040201
    secondary_diagonal = 0x102040810204080

    # corners without diagonals
    right_bottom = 0x80c0e0f0f8fcfe
    left_bottom = 0x103070f1f3f7f
    right_top = 0xfefcf8f0e0c08000
    left_top = 0x7f3f1f0f07030100

    left_coord = start_position % 8
    bottom_coord = start_position // 8

    if left_coord < bottom_coord:
        main_helper = left_top
        main_mask = ((main_diagonal >> abs(left_coord - bottom_coord)) & main_helper)
    elif left_coord == bottom_coord:
        main_mask = main_diagonal
    else:
        main_helper = right_bottom
        main_mask = ((main_diagonal << abs(left_coord - bottom_coord)) & main_helper)

    t = 7 - left_coord - bottom_coord
    if t == 0:
        secondary_mask = secondary_diagonal
    elif t < 0:
        secondary_helper = right_top
        secondary_mask = secondary_diagonal << abs(7 - left_coord - bottom_coord) & secondary_helper
    else:
        secondary_helper = left_bottom
        secondary_mask = secondary_diagonal >> abs(7 - left_coord - bottom_coord) & secondary_helper

    step_mask = (main_mask | secondary_mask) ^ figure_mask
    return step_mask


if __name__ == '__main__':
    mask = calculate_bishop_step_mask(14)
    print_chess_mask(mask)
