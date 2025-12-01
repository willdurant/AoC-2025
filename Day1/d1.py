def get_dial_index(
    instruction: str,
    dial_index: int,
) -> tuple[int, bool]:
    direction = 1 if instruction[0] == "R" else -1
    amount = int(instruction[1:])
    new_dial_index = (dial_index + direction * amount) % 100

    return new_dial_index, new_dial_index == 0


def main() -> None:
    zero_count = 0
    dial_index = 50

    txt_filename = "Day1/input.txt"
    with open(txt_filename, "r") as f:
        instructions = f.read().splitlines()

    for instruction in instructions:
        dial_index, hit_zero = get_dial_index(instruction, dial_index)
        zero_count += int(hit_zero)

    print(f"Final zero count: {zero_count}")


if __name__ == "__main__":
    main()
