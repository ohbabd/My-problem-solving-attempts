def cellular_automaton(string, pattern, n):
    rules_numbers = [[128, 'xxx'], [64, 'xx.'], [32, 'x.x'], [16, 'x..'],
                     [8, '.xx'], [4, '.x.'], [2, '..x'], [1, '...']]
    rules = {'...': '.', '..x': '.', '.x.': '.', '.xx': '.', 'x..': '.', 'x.x': '.', 'xx.': '.', 'xxx': '.'}
    while pattern != 0:
        for r in rules_numbers:
            if pattern - r[0] >= 0:
                rules[r[1]] = 'x'
                pattern -= r[0]
                break
    for i in range(n):
        ng = ""
        for j in range(len(string)):
            ng += rules[string[j - 1] + string[j] + string[(j+1) % len(string)]]
            j += 1
        string = ng
    return string

