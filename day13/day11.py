def draw(holes):
    max_x = 0
    max_y = 0
    for num in holes:
        x, y = num.split(",")
        x, y = int(x), int(y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    l = [["." for i in range(max_x + 1)] for _ in range(max_y + 1)]
    for num in holes:
        x, y = num.split(",")
        x, y = int(x), int(y)
        # print(x, max_x, y, max_y)
        l[y][x] = "#"
    for line in l:
        print(line)
    print("\n")


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        idx = lines.index("\n")
        holes, instructions = lines[:idx], lines[idx + 1:]

        holes = [i.strip() for i in holes]
        final_holes = holes.copy()

        for instruction in instructions:
            axis = instruction.split("=")
            axis, amount = axis[0][-1] == "y", int(axis[1])
            for index, hole in enumerate(holes):
                coord = int(hole.split(",")[axis])
                if coord > amount:
                    s = hole.split(",")
                    s[axis] = str(2 * amount - coord)
                    final_holes[index] = ",".join(s)
            holes = final_holes
            print(len(set(final_holes)))
        draw(final_holes)
        # answer is the first number printed and the final  code given to you


if __name__ == '__main__':
    main()

