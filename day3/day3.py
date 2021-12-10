def main():
    with open("input.txt", "r") as f:
        oxygen = [line.rstrip() for line in f]
        CO2 = oxygen

        f.seek(0)
        line_len = len(f.readline()) - 1
        # print(len(oxygen), oxygen)
        for i in range(line_len):
            count_oxygen = 0
            total_count_oxygen = 0
            count_CO2 = 0
            total_count_CO2 = 0
            for index, line in enumerate(oxygen):
                count_oxygen += line[i] == "1"
                total_count_oxygen += 1
            ox_truth_val = int(count_oxygen >= total_count_oxygen - count_oxygen)
            if len(oxygen) > 1:
                oxygen = [n for n in oxygen if n[i] == str(ox_truth_val)]
            for index, line in enumerate(CO2):
                count_CO2 += line[i] == "0"
                total_count_CO2 += 1
            CO2_truth_val = int(count_CO2 > total_count_CO2 - count_CO2)
            print(CO2_truth_val)
            if len(CO2) > 1:
                CO2 = [n for n in CO2 if n[i] == str(CO2_truth_val)]
            # debug = [c[i + 1] for c in CO2]
            # print(len(CO2), i, CO2_truth_val, list(zip(CO2, debug)))
            # print(oxygen == CO2, oxygen, CO2)
        print(int(oxygen[0], 2) * int(CO2[0], 2))


if __name__ == '__main__':
    main()


"""
part 1:
def main():
    with open("input.txt", "r") as f:
        line_len = len(f.readline()) - 1
        amounts = [0 for _ in range(line_len)]
        total = 0
        f.seek(0)
        for index, line in enumerate(f):
            for i, char in enumerate(line[:-1]):
                amounts[i] += char == "1"
            total += 1
        gamma = 0
        for n in amounts:
            gamma <<= 1
            gamma += n > total - n
        epsilon = 2 ** 12 - 1 - gamma
        print(f"{gamma:b}, {epsilon:b}")
        print(gamma * epsilon)



if __name__ == '__main__':
    main()

"""








