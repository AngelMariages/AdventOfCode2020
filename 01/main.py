def main():
    data = read_from_file_as_ints()

    results2 = find_2_num_that_sum_to_2020(data)
    results3 = find_3_num_that_sum_to_2020(data)

    print("Results for 2 found: {}".format(results2))
    print("Results for 3 found: {}".format(results3))


def read_from_file_as_ints(fileName="input.txt"):
    lines = []

    with open(fileName, "r") as f:
        for line in f:
            lines.append(int(line))

    return lines


def find_2_num_that_sum_to_2020(data):
    found = []
    results = []

    for idx, first in enumerate(data):
        rest = data[:idx] + data[idx+1:]

        if first in found:
            continue

        for second in rest:
            if (first + second) == 2020:
                print("{} + {} = 2020!".format(first, second))
                found.append(second)

                results.append(first * second)

    return results


def find_3_num_that_sum_to_2020(data):
    found = []
    results = []

    for idx, first in enumerate(data):
        rest = data[:idx] + data[idx+1:]

        if first in found:
            continue

        for idx2, second in enumerate(rest):
            rest2 = rest[:idx2] + rest[idx2+1:]

            if second in found:
                continue

            for third in rest2:
                if (first + second + third == 2020):
                    print("{} + {} + {} = 2020!".format(first, second, third))
                    found.extend([first, second, third])

                    results.append(first * second * third)

    return results


if __name__ == "__main__":
    main()
