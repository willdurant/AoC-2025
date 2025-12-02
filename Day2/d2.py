def sum_invalid_ids_in_range(id_range: str) -> int:
    start, end = (int(id) for id in id_range.split("-"))

    invalid_ids = list()
    for id in range(start, end + 1):
        str_id = str(id)
        no_digits = len(str_id)
        midpoint = len(str_id) // 2
        if no_digits % 2 != 0:
            continue

        if str_id[:midpoint] == str_id[midpoint:]:
            invalid_ids.append(id)

    return sum(invalid_ids)


def main() -> None:
    txt_filename = "Day2/input.txt"
    with open(txt_filename, "r") as f:
        ranges = f.read().split(",")

    total_invalid_id_sum = 0

    for id_range in ranges:
        invalid_id_sum = sum_invalid_ids_in_range(id_range)
        total_invalid_id_sum += invalid_id_sum

    print(f"Part 1: Total invalid id value is: {total_invalid_id_sum}")


if __name__ == "__main__":
    main()
