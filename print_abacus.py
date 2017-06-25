# This scripts prints the abacus visual representation of an integer


def zeros_adder(a):
    int_string = str(a)              # Creating a string with our integer's digits.
    while len(int_string) < 10:      # Adding enough zeros to teh string.
        int_string = '0' + int_string
    i = 0
    int_digits = [0] * 10            # Creating a list to store the digits.
    while i < 10:                    # putting digits in the list
        int_digits[i] = int(int_string[i])
        i = i + 1

    return int_digits


def print_abacus(a):
    num = zeros_adder(a)
    abacus = "00000*****"
    for i in num:
        print('|' + abacus[0:9-i] + "   " + abacus[9-i+1:] + '|')

