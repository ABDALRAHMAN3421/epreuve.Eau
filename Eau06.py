import sys

def capitalize_every_other(string):
    result = []
    capitalize = True  

    for char in string:
        if char.isalpha():  
            if capitalize:
                result.append(char.upper())
            else:
                result.append(char.lower())
            capitalize = not capitalize  
        else:
            result.append(char)  

    return ''.join(result)

def resolve(input_string):
    if isinstance(input_string, str):  
        return capitalize_every_other(input_string)
    else:
        return "Error: Input must be a string!"

    if len(sys.argv) > 1:
        string_to_process = sys.argv[1]
        print(resolve(string_to_process))
    else:
        print("Error: Please provide a string as a command-line argument.")
