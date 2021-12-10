def main():
    with open("input.txt", "r") as f:
        increases = 0
        sliding_window = []
        previous_window_sum = float("inf")
        for line in f:
            try:
                n = int(line)
                if len(sliding_window) == 3:
                    sliding_window = sliding_window[1:] + [n]
                    this_sum = sum(sliding_window)
                    increases += this_sum > previous_window_sum
                    previous_window_sum = this_sum
                else:
                    sliding_window.append(n)
            except ValueError:
                pass
        print(increases)


if __name__ == '__main__':
    main()


"""
answer for p1:
def main():
    with open("input.txt", "r") as f:
        increases = 0
        previous = float("inf")
        for line in f:
            try:
                n = int(line)
                increases += n > previous
                previous = n
            except ValueError:
                pass
        print(increases)

"""