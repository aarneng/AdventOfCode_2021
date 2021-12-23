from math import floor, ceil


def explode(inp):
    def add_left(lst, n):
        if n is None:
            return lst
        if isinstance(lst, list):
            return [add_left(lst[0], n), lst[1]]
        return lst + n

    def add_right(lst, n):
        if n is None:
            return lst
        if isinstance(lst, list):
            return [lst[0], add_right(lst[1], n)]
        return lst + n

    def inner(inp, depth=0):
        if isinstance(inp, int):
            return False, None, inp, None
        if depth >= 4:
            return True, inp[0], 0, inp[1]
        a, b = inp
        exploded, left, a, right = inner(a, depth + 1)
        if exploded:
            return True, left, [a, add_left(b, right)], None
        exploded, left, b, right = inner(b, depth + 1)
        if exploded:
            return True, None, [add_right(a, left), b], right
        return False, None, inp, None

    changed, _, ans, _ = inner(inp)
    return changed, ans
    # def inner(inp, depth, add_next=0):
    #     # print(depth, inp, add_next)
    #     to_add = 0, 0
    #     e = False
    #     if depth >= 4:
    #         print("depth exceede")
    #         buffer = inp
    #         inp = 0
    #         return inp, buffer[0], buffer[1], True
    #     if isinstance(inp[0], list) and not e:
    #         ans = inner(inp[0], depth + 1)
    #         e = ans[3]
    #         inp[0] = ans[0]
    #         if ans[0] == 0:
    #             to_add = ans[1], ans[2]
    #     elif isinstance(inp[0], int):
    #         inp[0] += add_next
    #         add_next = 0
    #     if isinstance(inp[1], list) and not e:
    #         ans = inner(inp[1], depth + 1, add_next)
    #         inp[1] = ans[0]
    #         if ans[0] == 0:
    #             if isinstance(inp[0], int):
    #                 inp[0] += ans[1]
    #             to_add = ans[1], ans[2]
    #             add_next = ans[3]
    #     elif isinstance(inp[1], int):
    #         inp[1] += to_add[1]
    #         to_add = to_add[0], 0
    #     # if isinstance(inp[1], list):
    #     #     inp[1] = inner(inp[1])
    #     return inp, to_add[0], to_add[1], add_next
    # return inner(inp, 0)[0]


def split(inp):
    def inner(inp, already_split=False):
        if isinstance(inp, int):
            return inp, already_split
        s = already_split
        if isinstance(inp[0], list):
            inp[0], _ = inner(inp[0])
        elif inp[0] >= 10 and not s:
            l = inp[0] / 2
            l = [floor(l), ceil(l)]
            inp[0] = l
            s = True
        if isinstance(inp[1], list):
            inp[1], _ = inner(inp[1], s)
        elif inp[1] >= 10 and not s:
            l = inp[1] / 2
            l = [floor(l), ceil(l)]
            inp[1] = l
            s = True
        return inp, s

    def inner2(x):
        if isinstance(x, int):
            if x >= 10:
                return True, [x // 2, ceil(x / 2)]
            return False, x
        a, b = x
        change, a = inner2(a)
        if change:
            return True, [a, b]
        change, b = inner2(b)
        return change, [a, b]

    # c1, c2 = inner(inp)
    # print(inp)
    # print("1", (c2, c1))
    # print("2", inner2(inp))
    # print(inp)
    return inner(inp)


def eval_number(inp) -> int:
    if isinstance(inp[0], list):
        left = 3 * eval_number(inp[0])
    else:
        left = 3 * inp[0]
    if isinstance(inp[1], list):
        right = 2 * eval_number(inp[1])
    else:
        right = 2 * inp[1]
    return left + right


def main():
    with open("input_test.txt", "r") as f:
        lines = [eval(l) for l in f.readlines()]
        ans = lines[0]
        # temp = [[[[0,7],4],[15,[0,13]]],[1,1]]
        # print(temp)
        # temp = split(temp)
        # print(temp)
        # temp = split(temp)
        # print(temp)
        # temp = split(temp)
        # print(explode(temp))

        for line in lines[1:]:
            ans = [ans, line]
            x = ans
            while True:
                change, x = explode(x)
                if change:
                    continue
                x, change = split(x)
                if not change:
                    break
            ans = x
            # did_change, ans = explode(ans)
            # while did_change:
            #     did_change, ans = explode(ans)
            #     if did_change:
            #         continue
            #     prev = ans
            #     ans = split(ans)
            #     if prev == ans:
            #         break
        print(eval_number(ans))


if __name__ == '__main__':
    main()

