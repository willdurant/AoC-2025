from functools import reduce


def get_max_joltage(bank: str) -> int:
    integers = [int(number) for number in bank]
    first_max = max(integers[:-1])
    first_max_idx = integers.index(first_max)
    second_max = max(integers[first_max_idx + 1 :])
    joltage = int(str(first_max) + str(second_max))
    return joltage


def get_max_joltage_12b(bank: str) -> int:
    integers = [int(number) for number in bank]

    maximums = list()
    maximum_indices = list()
    for i, space_required in enumerate(reversed(range(12))):
        start_idx = 0 if i == 0 else maximum_indices[i - 1] + 1
        end_idx = len(integers) - space_required
        chunk = integers[start_idx:end_idx]

        maximum = max(chunk)
        maximum_idx = start_idx + chunk.index(maximum)

        maximums.append(str(maximum))
        maximum_indices.append(maximum_idx)

    joltage = int(reduce(lambda x, y: x + y, maximums))
    return joltage


def test(input_value: str, expected_output: int) -> None:
    print(f"Part 2 Test: input: {input_value}, expected output: {expected_output}")
    calculated_joltage = get_max_joltage_12b(input_value)
    assert calculated_joltage == expected_output, (
        f"Test failed! Returned {calculated_joltage}"
    )
    print("Test passed!")


def main() -> None:
    txt_filename = "Day3/input.txt"
    with open(txt_filename, "r") as f:
        banks = f.read().splitlines()

    total_joltage = 0

    for bank in banks:
        joltage = get_max_joltage(bank)
        total_joltage += joltage

    print(f"Part 1: Total output voltage is: {total_joltage}")

    total_joltage = 0

    test("987654321111111", 987654321111)
    test("811111111111119", 811111111119)
    test("234234234234278", 434234234278)
    test("818181911112111", 888911112111)

    for bank in banks:
        joltage = get_max_joltage_12b(bank)
        total_joltage += joltage

    print(f"Part 2: Total output voltage is: {total_joltage}")


if __name__ == "__main__":
    main()
