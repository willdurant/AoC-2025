def identify_rolls(
    previous_row: list[str], current_row: list[str], next_row: list[str]
) -> tuple[int, str]:
    rolls_found = 0
    converted_row = []
    for i, option in enumerate(current_row):
        start = 0 if i == 0 else i - 1
        end = i + 2
        if option == "@":
            adjacency_area = (
                previous_row[start:end] + current_row[start:end] + next_row[start:end]
            )
            adjacency_area = [
                1 if selection == "@" else 0 for selection in adjacency_area
            ]
            total_adjacent = sum(adjacency_area) - 1
            if total_adjacent < 4:
                rolls_found += 1
                converted_row.append("x")
                continue

        converted_row.append(option)

    return rolls_found, "".join(converted_row)


def identify_all_rolls(rows: list[str]) -> tuple[int, str]:
    previous_row = []
    current_row = []
    next_row = []

    current_row = [option for option in rows[0]]
    rest_rows = rows[1:]
    rest_rows.append([])

    total_rolls_found = 0
    converted_rows = []
    for row in rest_rows:
        next_row = [option for option in row]

        rolls_found, converted_row = identify_rolls(previous_row, current_row, next_row)
        converted_rows.append(converted_row)
        total_rolls_found += rolls_found

        previous_row = current_row
        current_row = next_row

    return total_rolls_found, "\n".join(converted_rows)


def identify_all_rolls_iteration(rows: list[str]) -> tuple[int, str]:
    rows_to_iterate = rows
    keep_iterating = True

    total_rolls = 0
    while keep_iterating:
        total_rolls_found, test_output_str = identify_all_rolls(rows_to_iterate)
        total_rolls += total_rolls_found
        rows_to_iterate = test_output_str.splitlines()
        if total_rolls_found == 0:
            break

    return total_rolls, "\n".join(rows_to_iterate)


def main() -> None:
    test_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
    expected_output = 13
    print(f"Part 1 Test: input:\n{test_input}\nexpected output: {expected_output}")
    test_output, test_output_str = identify_all_rolls(test_input.splitlines())
    assert test_output == expected_output, f"Test failed! Returned {test_output}"
    print("Test passed!")

    txt_filename = "Day4/input.txt"
    with open(txt_filename, "r") as f:
        rows = f.read().splitlines()

    total_rolls_found, test_output_str = identify_all_rolls(rows)

    print(f"Part 1: Total rolls found: {total_rolls_found}")

    expected_output = 43
    print(f"Part 2 Test: input:\n{test_input}\nexpected output: {expected_output}")
    test_output, test_output_str = identify_all_rolls_iteration(test_input.splitlines())
    assert test_output == expected_output, f"Test failed! Returned {test_output}"
    print("Test passed!")

    total_rolls_found, test_output_str = identify_all_rolls_iteration(rows)
    print(f"Part 2: Total rolls found: {total_rolls_found}")


if __name__ == "__main__":
    main()
