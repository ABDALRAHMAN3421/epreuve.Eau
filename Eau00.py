def three_digit_combination():
    result = ''

    for number in range(48, 58): 
        for number2 in range(number + 1, 58):
            for number3 in range(number2 + 1, 58):
                result += chr(number) + chr(number2) + chr(number3) + ','

    return result[:-1]  

def error_without_argument(argument=None):
    if argument:
        print("Error: The argument is not necessary for this script.")
    else:
        print(three_digit_combination())

error_without_argument()

