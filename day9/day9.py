from collections import defaultdict


def can_go_to(x, y, basin_map, visited):
    if not (0 <= x < len(basin_map)) or not (0 <= y < len(basin_map[0])):
        return False
    if visited[(x, y)]:
        return False
    if basin_map[x][y]:
        return False
    return True


def find_basin_size(basin_map, visited, x, y):
    active = [(x, y)]
    visited[(x, y)] = True
    size = 1
    while active:
        cx, cy = active.pop()
        if can_go_to(cx + 1, cy, basin_map, visited):
            active.append((cx + 1, cy))
            visited[(cx + 1, cy)] = True
            size += 1
        if can_go_to(cx - 1, cy, basin_map, visited):
            active.append((cx - 1, cy))
            visited[(cx - 1, cy)] = True
            size += 1
        if can_go_to(cx, cy + 1, basin_map, visited):
            active.append((cx, cy + 1))
            visited[(cx, cy + 1)] = True
            size += 1
        if can_go_to(cx, cy - 1, basin_map, visited):
            active.append((cx, cy - 1))
            visited[(cx, cy - 1)] = True
            size += 1
    return size


def main():
    with open("input.txt", "r") as f:
        l = f.readlines()
        lines = [[int(i) for i in list(subline.strip())] for subline in l]
        basin_map = [[i == 9 for i in sublist] for sublist in lines]
        visited = defaultdict(lambda: False)
        sizes = []
        for i, sublist in enumerate(basin_map):
            for j, current_square in enumerate(sublist):
                if can_go_to(i, j, basin_map, visited):
                    basin_size = find_basin_size(basin_map, visited, i, j)
                    sizes.append(basin_size)
        biggest_3 = sorted(sizes, reverse=True)[:3]
        print(biggest_3[0] * biggest_3[1] * biggest_3[2])


if __name__ == '__main__':
    main()


"""
p1:
l = f.readlines()
lines = [[int(i) for i in list(subline.strip())] for subline in l]
s = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        min_point = True
        if x > 0:
            min_point = min_point and lines[y][x - 1] > lines[y][x]
        if x < len(lines[0]) - 1:
            min_point = min_point and lines[y][x] < lines[y][x + 1]
        if y > 0:
            min_point = min_point and lines[y - 1][x] > lines[y][x]
        if y < len(lines) - 1:
            min_point = min_point and lines[y][x] < lines[y + 1][x]
        s += (lines[y][x] + 1) * min_point
print(s)
"""