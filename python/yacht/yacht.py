# Score categories
# Change the values as you see fit
YACHT           = 50
ONES            = 1 
TWOS            = 2
THREES          = 3
FOURS           = 4
FIVES           = 5
SIXES           = 6
FULL_HOUSE      = 7
FOUR_OF_A_KIND  = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT    = 10
CHOICE          = 11


def score(dice, category):
    checker = len(set(dice)) 
    counts = dict()
    for roll in dice:
        if roll in counts:
            counts[roll] += 1
        else:
            counts[roll] = 1

    if category in [ONES, TWOS, THREES,FOURS,FIVES,SIXES]:
        score = 0
        for x in dice:
            # print(x)
            if x == category:
                score += 1
    
        score = score * category
        return score
    
    elif category == YACHT:
        if checker == 1:
            return 50
        return 0 
    elif category == FULL_HOUSE:
        if {2,3} != set(counts.values()):
            return 0
        return sum(dice)
    elif category == LITTLE_STRAIGHT:
        if sum(dice) == 15:
            return 30
        return 0
    elif category == BIG_STRAIGHT:
        if sum(dice) == 20:
            return 30
        return 0
    elif category == CHOICE:
        return sum(dice)
    elif category == FOUR_OF_A_KIND:
        for k, v in counts.items():
            if v >= 4:
                return k*4

        return 0
    else:
        return 0 #?? DEFAULT CASE ??
    
