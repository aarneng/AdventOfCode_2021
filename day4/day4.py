def is_winning_board(board):
    def helper(b):
        # print(b)
        # print(all(i is True for i in b[1]))
        # print([all(i) for i in b])
        return any([all(j is True for j in i) for i in b])

    return helper(board) or helper(list(zip(*board[::-1])))


def populate_with_guess(board, guess):
    for i, line in enumerate(board):
        for j, num in enumerate(line):
            if num == guess:
                board[i][j] = True
                break  # assuming each board only has each number once


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        input_nums = [int(i) for i in lines[0].split(",")]
        # print(input_nums)
        all_boards = []
        current_board = []

        for line in lines[2:]:
            if line == "\n":
                all_boards.append(current_board)
                current_board = []
            else:
                line = line.strip()
                nums = [int(i) for i in line.split(" ") if i != ""]
                current_board.append(nums)

        for i in range(5):
            for board in all_boards:
                populate_with_guess(board, input_nums[i])

        n_winning = 0
        for board in all_boards:
            if is_winning_board(board):
                n_winning += 1
        if n_winning == len(all_boards) - 1:
            for board in all_boards:
                if not is_winning_board(board):
                    sum_nums = sum([n for row in board for n in row if n is not True])
                    print(sum_nums * input_nums[4])
                    return

        for index, num in enumerate(input_nums[5:]):
            index += 5
            n_winning = 0
            for board in all_boards:
                populate_with_guess(board, num)
                if is_winning_board(board):
                    n_winning += 1
            if n_winning == len(all_boards) - 1:
                for board in all_boards:
                    if not is_winning_board(board):
                        i = 1
                        while not is_winning_board(board):
                            populate_with_guess(board, input_nums[index + i])
                            i += 1
                        sum_nums = sum([n for row in board for n in row if n is not True])
                        print(sum_nums * input_nums[index + i - 1])
                        print(board)
                        return
        print("toot")


if __name__ == '__main__':
    main()

"""
def is_winning_board(board):
    def helper(b):
        # print(b)
        # print(all(i is True for i in b[1]))
        # print([all(i) for i in b])
        return any([all(j is True for j in i) for i in b])

    return helper(board) or helper(list(zip(*board[::-1])))


def populate_with_guess(board, guess):
    for i, line in enumerate(board):
        for j, num in enumerate(line):
            if num == guess:
                board[i][j] = True
                break  # assuming each board only has each number once


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        input_nums = [int(i) for i in lines[0].split(",")]
        # print(input_nums)
        all_boards = []
        current_board = []

        for line in lines[2:]:
            if line == "\n":
                all_boards.append(current_board)
                current_board = []
            else:
                line = line.strip()
                nums = [int(i) for i in line.split(" ") if i != ""]
                current_board.append(nums)

        for i in range(5):
            for board in all_boards:
                populate_with_guess(board, input_nums[i])

        for board in all_boards:
            if is_winning_board(board):
                break_loop = True
                sum_nums = sum([n for row in board for n in row if n is not True])
                # print(sum_nums, input_nums[4])
                # print(board)
                return

        for num in input_nums[5:]:
            for board in all_boards:
                populate_with_guess(board, num)
                if is_winning_board(board):
                    sum_nums = sum([n for row in board for n in row if n is not True])
                    print(sum_nums * num)
                    print(board)
                    return


if __name__ == '__main__':
    main()

"""

