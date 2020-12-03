def main():
    legacy_valid = 0
    new_valid = 0
    data = read_lines_from_file()

    for d in data:
        val_legacy = is_valid_for_legacy(d)
        val_new = is_valid_for_new(d)

        if val_legacy:
            legacy_valid += 1
        if val_new:
            new_valid += 1

    print("Legacy valid passwords: {}".format(legacy_valid))
    print("New valid passwords: {}".format(new_valid))


def read_lines_from_file(fileName="input.txt"):
    lines = []

    with open(fileName, "r") as f:
        for line in f:
            lines.append(line.strip())

    return lines

def is_valid_for_new(line):
    splitted = line.split(': ')

    policy = splitted[0]
    pswd = splitted[1]

    p_char = get_policy_char(policy)
    p_1 = int(get_policy_first_num(policy))
    p_2 = int(get_policy_second_num(policy))

    first = ''
    second = ''

    if len(pswd) >= p_1:
        first = pswd[p_1-1]
    if len(pswd) >= p_2:
        second = pswd[p_2-1]

    if (first != second):
        if (first == p_char or second == p_char):
            return True

    return False

def is_valid_for_legacy(line):
    splitted = line.split(': ')

    policy = splitted[0]
    pswd = splitted[1]

    p_char = get_policy_char(policy)
    p_min = int(get_policy_first_num(policy))
    p_max = int(get_policy_second_num(policy))

    occurrences = get_occurrences_of_char(p_char, pswd)

    return p_min <= occurrences <= p_max


def get_policy_char(policy):
    return policy.split(' ')[1:].pop()


def get_policy_first_num(policy):
    return policy.split('-')[0:1].pop()


def get_policy_second_num(policy):
    return (policy.split('-')[:2].pop()).split(' ')[:1].pop()


def get_occurrences_of_char(char, pswd):
    occurrences = 0

    for c in pswd:
        if c == char:
            occurrences += 1

    return occurrences


if __name__ == "__main__":
    main()
