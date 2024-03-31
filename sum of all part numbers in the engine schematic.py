def is_valid_coordinate(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col

def sum_adjacent_numbers(schematic):
    symbols = ['*', '#', '+', '$']
    rows = len(schematic)
    cols = len(schematic[0])
    total_sum = 0

    for r in range(rows):
        for c in range(cols):
            if schematic[r][c].isdigit():
                adjacent = False
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_r, new_c = r + dr, c + dc
                    if is_valid_coordinate(new_r, new_c, rows, cols) and schematic[new_r][new_c] in symbols:
                        adjacent = True
                        break
                if adjacent:
                    total_sum += int(schematic[r][c])

    return total_sum

# Your engine schematic
schematic = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

total_part_numbers_sum = sum_adjacent_numbers(schematic)
print(f"The sum of all part numbers in the engine schematic is: {total_part_numbers_sum}")
