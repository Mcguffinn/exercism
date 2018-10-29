from itertools import permutations

def get_value(mapping, word):
    x = ""

    for ch in word:
        x += str(mapping[ch])
    
    if x.startswith('0'):
        raise Exception("NO!")

    return int(x)

def check_solution(alpha, puzzle):
    lhs, rhs = puzzle.split('==')
    terms = lhs.split('+')
    lhs_num = 0

    try:
        rhs_num = get_value(alpha, rhs.strip())
    except Exception:
        return False

    for term in terms:
        try:       
            lhs_num += get_value(alpha, term.strip())
        except Exception:
            return False

    return lhs_num == rhs_num

def solve(puzzle):
    chars = set()
    perm = permutations([0,1,2,3,4,5,6,7,8,9])

    for ch in puzzle:
        if ch in ["+", "=", " "]:
            continue
        chars.add(ch)

    keys = list(chars)

    for canidate in list(perm):
        alpha = dict(zip(keys, canidate))

        if check_solution(alpha, puzzle):
            return alpha
    
    return {}
