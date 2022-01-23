dice_value = 0
total_rolls = 0


def roll_dice(rolls=3):
    global dice_value, total_rolls
    score = 0
    for roll in range(rolls):
        dice_value = 1 + dice_value % 100
        score += dice_value
    total_rolls += rolls
    return score


def add_score(player_score, space):
    roll_amt = roll_dice()
    space = (space + roll_amt) % 10
    space += 10 * (space == 0)
    player_score += space
    return player_score, space


def main():
    global total_rolls
    with open("input.txt", "r") as f:
        p1, p2 = f.read().splitlines()
        p1 = int(p1[-1])
        p2 = int(p2[-1])
        p1_score, p2_score = 0, 0
        while p1_score < 1000 and p2_score < 1000:
            p1_score, p1 = add_score(p1_score, p1)
            if p1_score >= 1000:
                break
            p2_score, p2 = add_score(p2_score, p2)
        print(min(p1_score, p2_score) * total_rolls)


if __name__ == '__main__':
    main()

"""
dice_value = 0
total_rolls = 0


def roll_dice(rolls=3):
    global dice_value, total_rolls
    score = 0
    for roll in range(rolls):
        dice_value = 1 + dice_value % 100
        score += dice_value
    total_rolls += rolls
    return score


def add_score(player_score, space):
    roll_amt = roll_dice()
    space = (space + roll_amt) % 10
    space += 10 * (space == 0)
    player_score += space
    return player_score, space


def main():
    global total_rolls
    with open("input.txt", "r") as f:
        p1, p2 = f.read().splitlines()
        p1 = int(p1[-1])
        p2 = int(p2[-1])
        p1_score, p2_score = 0, 0
        while p1_score < 1000 and p2_score < 1000:
            p1_score, p1 = add_score(p1_score, p1)
            if p1_score >= 1000:
                break
            p2_score, p2 = add_score(p2_score, p2)
        print(min(p1_score, p2_score) * total_rolls)


if __name__ == '__main__':
    main()


"""