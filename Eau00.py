def three_digit_combination():
    result = ''

    for number in range(48, 58): 
        for number2 in range(number + 1, 58):  
            for number3 in range(number2 + 1, 58):  
                result += str(number - 48) + str(number2 - 48) + str(number3 - 48) + ','

    return result[:-1]  

def main():
    user_input = input("Please enter some input: ")
    if not user_input():
        print("Error: No arguments provided. Please provide input.")
        return  
    
    result = three_digit_combination()
    print(result)
