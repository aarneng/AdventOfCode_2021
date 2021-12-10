def minimise(nums, min_num, max_num):
    smallest_val_achieved = float("Inf")
    smallest_num = None
    for x in range(min_num, max_num + 1):
        f_x = 0
        for i in nums:
            fuel_cost = abs(x - i)
            fuel_cost = (fuel_cost + 1) * fuel_cost // 2
            # print(i, fuel_cost)
            f_x += fuel_cost
        # print(x, f_x)
        # print()
        if f_x < smallest_val_achieved:
            smallest_val_achieved = f_x
            smallest_num = x
    return smallest_num, smallest_val_achieved


def main():
    with open("input.txt", "r") as f:
        nums = [int(i) for i in f.readlines()[0].split(",")]
        print(minimise(nums, min(nums), max(nums)))


if __name__ == '__main__':
    main()


"""
p1:
def minimise(nums, min_num, max_num):
    smallest_val_achieved = float("Inf")
    smallest_num = None
    for x in range(min_num, max_num + 1):
        f_x = 0
        for i in nums:
            f_x += abs(x - i)
        if f_x < smallest_val_achieved:
            smallest_val_achieved = f_x
            smallest_num = x
    return smallest_num, smallest_val_achieved

"""