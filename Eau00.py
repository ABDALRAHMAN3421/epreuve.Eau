def three_digit_combination():
    result = []
    
    for number in range(0, 10):  
        for number2 in range(number + 1, 10):  
            for number3 in range(number2 + 1, 10):  
                result.append(f"{number}{number2}{number3}")  
    
    return ','.join(result)  

def main():
    user_input = input("Please enter some input: ")
    if not user_input:
        print("Error: No arguments provided. Please provide input.")
        return  
    
    result = three_digit_combination()
    print(result)


