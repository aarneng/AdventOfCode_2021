def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        point_mapping = {
            "(": 1,
            "[": 2,
            "{": 3,
            "<": 4
        }
        points = []
        for line in lines:
            autocomplete_points = 0
            prev_line = line
            line = line.strip()
            while line != prev_line and line:
                prev_line = line
                line = line.replace("()", "")
                line = line.replace("[]", "")
                line = line.replace("{}", "")
                line = line.replace("<>", "")

            uncorrupted = True
            for char in line:
                if char not in point_mapping.keys():
                    uncorrupted = False
                    break
            if not uncorrupted:
                continue

            for char in line[::-1]:
                autocomplete_points = autocomplete_points * 5 + point_mapping[char]
            # print(autocomplete_points)
            points.append(autocomplete_points)
        points = sorted(points)
        print(points[len(points) // 2])


if __name__ == '__main__':
    main()


"""
p1:

with open("input.txt", "r") as f:
    lines = f.readlines()
    point_mapping = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    syntax_errors_sum = 0
    for line in lines:
        prev_line = line
        line = line.strip()
        while line != prev_line and line:
            prev_line = line
            line = line.replace("()", "")
            line = line.replace("[]", "")
            line = line.replace("{}", "")
            line = line.replace("<>", "")
        for char in line:
            if char in point_mapping.keys():
                syntax_errors_sum += point_mapping[char]
                # print(char)
                break
    print(syntax_errors_sum)


"""