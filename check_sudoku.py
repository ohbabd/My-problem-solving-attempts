# This functions checks if a given sudoku solution is valid
def check_sudoku(solution):
    digit = 1
    dim = len(solution[0])
    while digit <= dim:
        i = 0
        while i < dim:
            count = 0
            j = 0
            while j < dim:
                if solution[i][j] == digit:
                    count += 1
                if solution[j][i] == digit:
                    count += 1
                j += 1
            if count != 2:
                return False
            i += 1
        digit += 1
    return True
