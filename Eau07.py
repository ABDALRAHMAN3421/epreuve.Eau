import sys

def capitalize_first_letter(string):
    if any(char.isdigit() for char in string):  
        return "Error: The string contains numbers."
    
    result = ""
    new_word = True  

    for char in string:
        if char.isspace():  
            result += char
            new_word = True  
        elif new_word:  
            result += char.upper()
            new_word = False  
        else:  
            result += char.lower()
    
    return result

def main():
    if len(sys.argv) < 2:
        print("Error: No input provided", file=sys.stderr)
        return
    
    input_string = " ".join(sys.argv[1:])  
    result = capitalize_first_letter(input_string)
    print(result)

main()
