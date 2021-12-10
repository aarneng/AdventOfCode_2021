def main():
    with open("input.txt", "r") as f:
        board = [[0 for _ in range(1000)] for _ in range(1000)]
        for line in f:
            x1, y1, x2, y2 = [int(j) for i in line.split(" -> ") for j in i.split(",")]
            if not (x1 == x2 or y1 == y2):
                dy = (y2 > y1) * 2 - 1
                dx = (x2 > x1) * 2 - 1
                while x1 != x2:
                    board[x1][y1] += 1
                    x1 += dx
                    y1 += dy
                board[x1][y1] += 1
                continue
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            # print(x1, x2, y1, y2)
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    board[x][y] += 1

        # for line in [i[0:10] for i in board[0:10]]:
        #     print(line)
        count = 0
        for line in board:
            for num in line:
                count += num >= 2
        print(count)


if __name__ == '__main__':
    main()

"""
def main():
    with open("input.txt", "r") as f:
        board = [[0 for _ in range(1000)] for _ in range(1000)]
        for line in f:
            x1, y1, x2, y2 = [int(j) for i in line.split(" -> ") for j in i.split(",")]

            if not (x1 == x2 or y1 == y2):
                continue
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            # print(x1, x2, y1, y2)
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    board[x][y] += 1
        count = 0
        for line in board:
            for num in line:
                count += num >= 2
        print(count)


if __name__ == '__main__':
    main()

"""