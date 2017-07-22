# This function checks if an element is a whole number between 1 and n (n = sudoku dimension)
def check_num(x, r):
    strX = str(x)
    i = 0
    count = 0
    while i < len(strX):    # goes through each character of the string
        if strX[i] in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):  # checks if the character represents a digit
            count+= 1
        i += 1
    return x <= r and count == len(strX)  # "x <= r" to see if the number is between 1 and n


# This functions checks if a given sudoku solution is valid
def check_sudoku(solution):
    dim = len(solution[0])
    i = 0
    # We basically gonna go through every element of the list
    while i < dim:  # So this goes through every row
        for e in solution[i]:  # And this geos through every column
            j = 0
            count = 0
            while j < dim:  # Goes through the row and the column containing the element we're testing
                if check_num(solution[i][j], dim) and check_num(solution[j][i], dim):
                    if solution[i][j] == e:
                        count += 1
                    if solution[j][i] == e:
                        count += 1
                j += 1
            if count != 2:
                return False
        i += 1
    return True
