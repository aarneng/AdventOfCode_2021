from collections import Counter, defaultdict


def window(seq, n=2):
    """Returns a sliding window (of width n) over data from the iterable"""
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    ret = [None for _ in range(len(seq) - n + 1)]
    for i in range(len(seq) - n + 1):
        ret[i] = seq[i: i + n]
    return ret


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        idx = lines.index("\n")
        string, instructions = lines[:idx][0].strip(), lines[idx + 1:]
        days = 40

        mapping = {}
        amounts = dict(Counter(window(string)))

        for instruction in instructions:
            l, r = instruction.strip().split(" -> ")
            mapping[l] = l[0] + r + l[1]

        for day in range(days):
            amounts_copy = defaultdict(lambda: 0)

            for k, v in amounts.items():
                next_vals = mapping[k]
                amounts_copy[next_vals[:2]] += v
                amounts_copy[next_vals[1:]] += v
            amounts = amounts_copy

        counts = defaultdict(lambda: 0)
        for k, v in amounts_copy.items():
            counts[k[0]] += v
            counts[k[1]] += v

        counts = counts.values()
        print(max(counts) // 2 - min(counts) // 2 + 1)


if __name__ == '__main__':
    main()

