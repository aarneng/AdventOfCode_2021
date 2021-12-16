from collections import defaultdict


def adjacent_square_coords(current, max):
    ret = []
    if current[0] > 0:
        ret.append((current[0] - 1, current[1]))
    if current[1] > 0:
        ret.append((current[0], current[1] - 1))
    if current[0] < max[0]:
        ret.append((current[0] + 1, current[1]))
    if current[1] < max[1]:
        ret.append((current[0], current[1] + 1))
    return ret


def expand_horizontal(lst, n=4):
    ret = lst
    for _ in range(n):
        lst = [(i % 9) + 1 for i in lst]
        ret += lst
    return ret


def expand_vertical(lst, n=4):
    ret = lst
    for _ in range(n):
        lst = [[(i % 9) + 1 for i in sublist] for sublist in lst]
        ret += lst
    return ret


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        lines = [[int(i) for i in sublist.strip()] for sublist in lines]
        lines = [expand_horizontal(line) for line in expand_vertical(lines)]

        # print([expand_horizontal(line, 1) for line in expand_vertical([[1, 2, 3], [4, 6, 5]], 1)])
        # print()
        # for line in lines:
        #     print(line)

        distances = defaultdict(lambda: float("inf"))

        current_square = (0, 0)
        distances[current_square] = 0
        unvisited = {(0, 1): (0, 0), (1, 0): (0, 0)}
        end_square = (len(lines[0]) - 1, len(lines) - 1)

        while current_square != end_square:
            min_next_dist = float("inf")
            next_square = None
            for square, adjacent_to in unvisited.items():
                dist = distances[adjacent_to] + lines[square[1]][square[0]]
                if dist < min_next_dist:
                    min_next_dist = dist
                    next_square = square

            current_square = next_square
            neighbours = adjacent_square_coords(current_square, end_square)
            for neighbour in neighbours:
                y, x = neighbour[0], neighbour[1]
                if distances[neighbour] > min_next_dist + lines[x][y]:
                    unvisited[neighbour] = current_square
                    distances[neighbour] = min_next_dist + lines[x][y]
            del unvisited[current_square]
            distances[current_square] = min_next_dist
        print(distances[end_square])


if __name__ == '__main__':
    main()

