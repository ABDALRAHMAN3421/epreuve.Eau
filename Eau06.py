import sys

def alternate_case(word):
    if not word:
        return None, "Input is empty"
    
    word = list(word.lower())  

    for i in range(0, len(word), 2):
        word[i] = word[i].upper()  

    word = ''.join(word)  

    if word.isdigit():
        return None, "error"
    else:
        return word, None

def get_user_input(prompt):
    user_input = input(prompt)
    if user_input:
        return user_input
    else:
        return None

def main():
    word = get_user_input('Enter your word: ')

    if word is None:
        print("Error in input. Exiting.")
        return
    result, error = alternate_case(word)
    if error:
        print(error, file=sys.stderr)
    else:
        print("Your result is: " + result)

main()
