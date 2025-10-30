import random
from random import randint

def main():
    cards = {i for i in range(52)}
    print(search(cards, 100000))


def search(cards, size):
    poker_hands = {
        "high_card": 0,
        "one_pair": 0,
        "two_pair": 0,
        "three_of_a_kind": 0,
        "straight": 0,
        "flush": 0,
        "full_house": 0,
        "four_of_a_kind": 0,
        "straight_flush": 0,
        "royal_flush": 0
    }

    for _ in range(size):
        # draw 5 random distinct cards (0–51)
        mycards = set(random.sample(list(cards), 5))
        tree = 0
        while True:
            match tree:
                case 0:
                    if colour(mycards.copy()):
                        tree = 1
                    else:
                        tree = 2
                case 1:
                    if order(mycards.copy()):
                        if royalFlush(mycards.copy()):
                            tree = 3
                        else:
                            tree = 4
                    else:
                        tree = 5
                case 2:
                    if row(mycards.copy(), 2) < 15:
                        tree = 6
                    else:
                        tree = 7
                case 3:
                    poker_hands["royal_flush"] += 1
                    break
                case 4:
                    poker_hands["straight_flush"] += 1
                    break
                case 5:
                    poker_hands["flush"] += 1
                    break
                case 6:
                    if zweiPaare(mycards.copy()):
                        tree = 8
                    elif row(mycards.copy(), 3) < 15:
                        tree = 9
                    elif row(mycards.copy(), 4) < 15:
                        tree = 10
                    elif fullHouse(mycards.copy()):
                        tree = 11
                    else:
                        tree = 14
                case 7:
                    if order(mycards.copy()):
                        tree = 12
                    else:
                        tree = 13
                case 8:
                    poker_hands["two_pair"] += 1
                    break
                case 9:
                    poker_hands["three_of_a_kind"] += 1
                    break
                case 10:
                    poker_hands["four_of_a_kind"] += 1
                    break
                case 11:
                    poker_hands["full_house"] += 1
                    break
                case 12:
                    poker_hands["straight"] += 1
                    break
                case 13:
                    poker_hands["high_card"] += 1
                    break
                case 14:
                    poker_hands["one_pair"] += 1
                    break

    # convert counts to percentages
    for key in poker_hands:
        poker_hands[key] = poker_hands[key] / size

    return poker_hands


def fullHouse(mycards):
    # dummy safe version to avoid crashes
    return False


def order(mycards):
    cards = sorted([c % 13 for c in mycards])
    return all(cards[i] + 1 == cards[i + 1] for i in range(4))


def royalFlush(mycards):
    cards = [c % 13 for c in mycards]
    return set(cards) == {0, 9, 10, 11, 12}


def zweiPaare(mycards):
    ranks = [c % 13 for c in mycards]
    pairs = [r for r in set(ranks) if ranks.count(r) == 2]
    return len(pairs) == 2


def row(mycards, x):
    ranks = [c % 13 for c in mycards]
    for r in ranks:
        if ranks.count(r) == x:
            return r
    return 15


def colour(mycards):
    suits = [c // 13 for c in mycards]
    return len(set(suits)) == 1


if __name__ == '__main__':
    main()
