def main():
    with open("input_test.txt", "r") as f:
        lines = f.read().splitlines()
        on_vals = {}
        for i, line in enumerate(lines):
            on = line[1] == "n"
            x, y, z = line.split(",")
            x = [int(i) for i in x.split("=")[1].split("..")]
            y = [int(i) for i in y.split("=")[1].split("..")]
            z = [int(i) for i in z.split("=")[1].split("..")]
            print(x, y, z)
            for xv in range(x[0], x[1] + 1):
                # if not -50 <= xv <= 50:
                #     continue
                for yv in range(y[0], y[1] + 1):
                    # if not -50 <= yv <= 50:
                    #     continue
                    for zv in range(z[0], z[1] + 1):
                        # if not -50 <=

                        on_vals[(xv, yv, zv)] = on
        print(list(on_vals.values()).count(True))


if __name__ == '__main__':
    main()

"""


"""