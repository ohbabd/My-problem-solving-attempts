def rule(n):
    rules_numbers = [[128, 'xxx'], [64, 'xx.'], [32, 'x.x'], [16, 'x..'],
                     [8, '.xx'], [4, '.x.'], [2, '..x'], [1, '...']]
    rules = {'...': '.', '..x': '.', '.x.': '.', '.xx': '.', 'x..': '.', 'x.x': '.', 'xx.': '.', 'xxx': '.'}
    while n != 0:
        for r in rules_numbers:
            if n - r[0] >= 0:
                rules[r[1]] = 'x'
                n -= r[0]
                break
    return rules


def cellular_automaton(string, pattern, n):
    if n == 0:
        return string
    rules = rule(pattern)
    ng = ""
    for j in range(len(string)):
        nxt = j + 1
        if j == len(string) - 1:
            nxt = 0
        ng += rules[string[j - 1] + string[j] + string[nxt]]
        j += 1
    return cellular_automaton(ng, pattern, n - 1)

