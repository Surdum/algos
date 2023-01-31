from bit_chess.utils import count_non_zero_bits_2, load_input_data, load_output_data
from bit_chess.figures.knight import calculate_knight_step_mask


test_data_set_path = 'tests'
test_data_set_len = 10

for i in range(test_data_set_len):
    knight_position = load_input_data(test_data_set_path, f'test.{i}.in')
    bit_count, mask = load_output_data(test_data_set_path, f'test.{i}.out')

    step_mask = calculate_knight_step_mask(knight_position)
    my_bit_count = count_non_zero_bits_2(step_mask)

    assert step_mask == mask, f'{step_mask} != {mask}'
    assert bit_count == my_bit_count, f'{my_bit_count} != {bit_count}'
    print(f'test {i} success')





