def main():
    depth = 0
    horizontal_position = 0
    aim = 0
    with open("input.txt", "r") as f:
        for line in f:
            try:
                l = line.split(" ")
                if l[0] == "forward":
                    horizontal_position += int(l[1])
                    depth += aim * int(l[1])
                elif l[0] == "down":
                    aim += int(l[1])
                elif l[0] == "up":
                    aim -= int(l[1])
            except ValueError:
                pass
        print(depth * horizontal_position)


if __name__ == '__main__':
    main()


"""
part 1
def main():
    depth = 0
    horizontal_position = 0
    with open("input.txt", "r") as f:
        for line in f:
            try:
                l = line.split(" ")
                if l[0] == "forward":
                    horizontal_position += int(l[1])
                elif l[0] == "down":
                    depth += int(l[1])
                elif l[0] == "up":
                    depth -= int(l[1])
            except ValueError:
                pass
        print(depth * horizontal_position)


if __name__ == '__main__':
    main()

"""
