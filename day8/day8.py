from collections import defaultdict


input_mapping = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}
input_mapping_reverse = {v: k for k, v in input_mapping.items()}


def difference_of_2_strs(a: str, b: str):
    a = set(a)
    b = set(b)
    if len(a) > len(b):
        return "".join(a.difference(b))
    return "".join(b.difference(a))


def find_mapping(input_strs: str) -> dict:
    input_strs = input_strs.strip().split(" ")

    answer_mapping = {}
    inputs_by_len = defaultdict(list)
    tmp = []
    for word in input_strs:
        inputs_by_len[len(word)].append(word)

    for i in [2, 3, 4, 7]:
        tmp.append(inputs_by_len[i][0])
    tmp = sorted(tmp, key=len)
    mapping_of_a = difference_of_2_strs(tmp[0], tmp[1])
    answer_mapping[mapping_of_a] = "a"

    cf = tmp[0]
    bd = difference_of_2_strs(tmp[0], tmp[2])
    eg = difference_of_2_strs("abcdefg", tmp[1] + tmp[2])

    b, e = "", ""
    for word in inputs_by_len[5]:
        amt_cf = 0
        for char in word:
            if char in cf:
                amt_cf += 1
        if amt_cf == 2:
            for char in word:
                if char in bd:
                    answer_mapping[char] = "d"
                    remaining_2 = difference_of_2_strs("abcdefg", word)
                    if remaining_2[0] in bd:
                        answer_mapping[remaining_2[0]] = "b"
                        b = remaining_2[0]
                    else:
                        answer_mapping[remaining_2[1]] = "b"
                        b = remaining_2[1]
                if char in eg:
                    answer_mapping[char] = "g"
                    remaining_2 = difference_of_2_strs("abcdefg", word)
                    if remaining_2[0] in eg:
                        answer_mapping[remaining_2[0]] = "e"
                        e = remaining_2[0]
                    else:
                        answer_mapping[remaining_2[1]] = "e"
                        e = remaining_2[1]
    for word in inputs_by_len[5]:
        amt_bd, amt_eg = 0, 0
        for char in word:
            if char in bd:
                amt_bd += 1
            if char in eg:
                amt_eg += 1
        if amt_bd == 2:
            for char in word:
                if char in cf:
                    remaining_2 = difference_of_2_strs("abcdefg", word)
                    remaining = difference_of_2_strs(remaining_2, e)
                    answer_mapping[remaining] = "c"
                    last_one = "".join(answer_mapping.keys())
                    last_one = difference_of_2_strs("abcdefg", last_one)
                    answer_mapping[last_one] = "f"
            break
        if amt_eg == 2:
            for char in word:
                if char in cf:
                    remaining_2 = difference_of_2_strs("abcdefg", word)
                    remaining = difference_of_2_strs(remaining_2, b)

                    answer_mapping[remaining] = "f"
                    last_one = "".join(answer_mapping.keys())
                    last_one = difference_of_2_strs("abcdefg", last_one)
                    answer_mapping[last_one] = "c"
            break

    return answer_mapping


def main():
    with open("input.txt", "r") as f:
        lines = [i.split("|") for i in f.readlines()]
        inputs, outputs = zip(*lines[::-1])
        sum_nums = 0
        for index, line in enumerate(inputs):
            correct_map = find_mapping(line)
            num = 0
            for word in outputs[index].strip().split(" "):
                actual = ""
                for char in word:
                    actual += correct_map[char]
                actual = "".join(sorted(actual))
                num = num * 10 + input_mapping_reverse[actual]
            sum_nums += num
        print(sum_nums)


if __name__ == '__main__':
    main()


"""
p1:
def main():
    with open("input.txt", "r") as f:
        lines = [i.split("|") for i in f.readlines()]
        inputs, outputs = list(zip(*lines[::-1]))
        count = 0
        unique_divisor_amts = [2, 3, 4, 7]
        for output in outputs:
            for word in output.strip().split(" "):
                l = len(word)
                for i in unique_divisor_amts:
                    if l == i:
                        count += 1
        print(count)

"""