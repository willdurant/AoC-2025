def identify_rolls(
    previous_row: list[str], current_row: list[str], next_row: list[str]
) -> int:
    rolls_found = 0
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

    return rolls_found


def identify_all_rolls(rows: list[str]) -> int:
    previous_row = []
    current_row = []
    next_row = []

    current_row = [option for option in rows[0]]
    rest_rows = rows[1:]
    rest_rows.append([])

    total_rolls_found = 0
    for row in rest_rows:
        next_row = [option for option in row]

        rolls_found = identify_rolls(previous_row, current_row, next_row)
        total_rolls_found += rolls_found

        previous_row = current_row
        current_row = next_row

    return total_rolls_found


def main() -> None:
    test_input = """..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.""".splitlines()
    expected_output = 13
    print(f"Part 2 Test: input:\n{test_input}\nexpected output: {expected_output}")
    test_output = identify_all_rolls(test_input)
    assert test_output == expected_output, f"Test failed! Returned {test_output}"
    print("Test passed!")

    txt_filename = "Day4/input.txt"
    with open(txt_filename, "r") as f:
        rows = f.read().splitlines()

    total_rolls_found = identify_all_rolls(rows)

    print(f"Part 1: Total rolls found: {total_rolls_found}")


if __name__ == "__main__":
    main()
