def get_dial_index(
    instruction: str,
    dial_index: int,
) -> tuple[int, bool]:
    direction = 1 if instruction[0] == "R" else -1
    amount = int(instruction[1:])
    new_dial_index = (dial_index + direction * amount) % 100

    return new_dial_index, new_dial_index == 0


def count_zero_hits(
    instruction: str,
    dial_index: int,
) -> tuple[int, int]:
    direction = 1 if instruction[0] == "R" else -1
    amount = int(instruction[1:])
    new_dial_index = (dial_index + direction * amount) % 100

    if direction == 1:
        distance_to_zero = (100 - dial_index) % 100
    else:
        distance_to_zero = dial_index % 100

    if distance_to_zero == 0:
        zero_hits = amount // 100
        return new_dial_index, zero_hits

    if amount < distance_to_zero:
        return new_dial_index, 0

    remaining = amount - distance_to_zero
    extra_hits = remaining // 100
    zero_hits = 1 + extra_hits

    return new_dial_index, zero_hits


def main() -> None:
    zero_count = 0
    dial_index = 50

    txt_filename = "Day1/input.txt"
    with open(txt_filename, "r") as f:
        instructions = f.read().splitlines()

    for instruction in instructions:
        dial_index, hit_zero = get_dial_index(instruction, dial_index)
        zero_count += int(hit_zero)

    print(f"Part 1: Final zero count: {zero_count}")

    zero_count = 0
    dial_index = 50
    for instruction in instructions:
        dial_index, passes = count_zero_hits(instruction, dial_index)
        zero_count += passes

    print(f"Part 2: Final zero count: {zero_count}")


if __name__ == "__main__":
    main()
