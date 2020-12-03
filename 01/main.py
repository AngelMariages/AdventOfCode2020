example = (1721, 979, 366, 299, 675, 1456)


def main():
    data = read_from_file_as_ints()

    #find_from(example)
    find_from(data)


def read_from_file_as_ints(fileName = "input.txt"):
    lines = []

    with open(fileName, "r") as f:
        for line in f:
            lines.append(int(line))

    return lines

def find_from(data):
    found2 = []
    found3 = []
    results2 = []
    results3 = []

    for idx, first in enumerate(data):
        rest = data[:idx] + data[idx+1:]

        if first in found2:
            continue

        for idx2, second in enumerate(rest):
            if (first + second) == 2020:
                print("{} + {} = 2020!".format(first, second))
                found2.append(second)

                results2.append(first * second)

            rest2 = data[:idx2] + data[idx2+1:]

            if second in found3:
                continue

            for third in rest2:
                if (first + second + third) == 2020:
                    print("{} + {} + {} = 2020!".format(first, second, third))
                    found3.append(first)
                    found3.append(second)
                    found3.append(third)

                    results3.append(first * second * third)

    print("Results for 2 found: {}".format(results2))
    print("Results for 3 found: {}".format(results3))

if __name__ == "__main__":
    main()
