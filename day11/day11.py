from collections import defaultdict


flashed = defaultdict(lambda: False)


def flash(x, y, lines):
    total_flashes = 0
    for dx in (-1, 0, 1):
        if 0 > x + dx or x + dx >= len(lines[0]):
            continue
        for dy in (-1, 0, 1):
            if 0 > y + dy or y + dy >= len(lines):
                continue
            if lines[x  + dx][y + dy] == 9:
                if flashed[(x + dx, y + dy)]:
                    continue
                flashed[(x + dx, y + dy)] = True
                total_flashes += 1 + flash(x + dx, y + dy, lines)
                lines[x + dx][y + dy] = 0
            else:
                lines[x + dx][y + dy] += 1
    return total_flashes


def main():
    with open("input.txt", "r") as f:
        lines = [[int(i) for i in list(subline.strip())] for subline in f.readlines()]

        total_flashes = 0

        day = 0

        while True:
            for x, line in enumerate(lines):
                for y, square in enumerate(line):
                    if square == 9:
                        flashed[(x, y)] = True
                        total_flashes += 1 + flash(x, y, lines)
                    else:
                        lines[x][y] += 1
            day += 1
            if len(flashed.keys()) == len(lines) * len(lines[0]):
                print(day)
                return
            for x, y in flashed.keys():
                lines[x][y] = 0
            flashed.clear()


if __name__ == '__main__':
    main()


"""
p1:

from collections import defaultdict


flashed = defaultdict(lambda: False)


def flash(x, y, lines):
    total_flashes = 0
    for dx in (-1, 0, 1):
        if 0 > x + dx or x + dx >= len(lines[0]):
            continue
        for dy in (-1, 0, 1):
            if 0 > y + dy or y + dy >= len(lines):
                continue
            if lines[x  + dx][y + dy] == 9:
                if flashed[(x + dx, y + dy)]:
                    continue
                flashed[(x + dx, y + dy)] = True
                total_flashes += 1 + flash(x + dx, y + dy, lines)
                lines[x + dx][y + dy] = 0
            else:
                lines[x + dx][y + dy] += 1
    return total_flashes


def main():
    with open("input.txt", "r") as f:
        lines = [[int(i) for i in list(subline.strip())] for subline in f.readlines()]

        total_flashes = 0

        days = 100

        for _ in range(days):
            for x, line in enumerate(lines):
                for y, square in enumerate(line):
                    if square == 9:
                        flashed[(x, y)] = True
                        total_flashes += 1 + flash(x, y, lines)
                    else:
                        lines[x][y] += 1
            for x, y in flashed.keys():
                lines[x][y] = 0
            flashed.clear()
        print(total_flashes)
"""