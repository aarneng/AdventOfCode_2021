def check_velocity(ix, iy, boundx, boundy):
    pos = [0, 0]
    maxy = 0
    miny = min(boundy)
    maxx = max(boundx)
    while pos[0] < maxx and pos[1] > miny:
        pos[0] += ix
        pos[1] += iy
        maxy = max(maxy, pos[1])
        ix = max(ix - 1, 0)
        iy -= 1
        if boundx[0] <= pos[0] <= boundx[1] and boundy[0] <= pos[1] <= boundy[1]:
            return maxy
    return -1


def main():
    with open("input.txt", "r") as f:
        l = f.readline()
        l = l.split(",")
        x = l[0].split("=")[1].split("..")
        y = l[1].split("=")[1].split("..")
        x = [int(i) for i in x]
        y = [int(i) for i in y]
        maxy = 0
        amt_successful = 0
        for init_x in range(2, 500):
            for init_y in range(-500, 500):
                # brute force this bad girl
                ans = check_velocity(init_x, init_y, x, y)
                maxy = max(maxy, ans)
                amt_successful += ans > -1
        print("part 1", maxy)
        print("part 2", amt_successful)


if __name__ == '__main__':
    main()

