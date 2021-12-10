def main():
    with open("input_test.txt", "r") as f:
        l = [int(i) for i in f.readline().split(",")]

        nums = {}

        for i in range(10):
            nums[i] = 0

        for item in l:
            nums[item] += 1

        for _ in range(256):
            amt_0 = None
            for i in range(9):
                # if i == 0:
                #     nums[8] = nums[i]
                if amt_0 is None:
                    amt_0 = nums[0]
                nums[i] = nums[i + 1]
            nums[8] = amt_0
            nums[6] += amt_0

        s = 0
        for n in nums.values():
            s += n
        print(s)


if __name__ == '__main__':
    main()
