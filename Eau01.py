import sys

def reverse_phrase(words):
    return ' '.join(words[::-1])

def get_input():
    if len(sys.argv) > 2:
        return ' '.join(sys.argv[2:])
    else:
        return input("Enter a phrase please: ")

def display_result(phrase):
    print("Reversed Phrase:")
    for word in phrase.split():
        print(word)

def handle_error(message):
    print(f"Error: {message}")

def command_line_argument():
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ['true', '1', 'yes', 'y']:
            return True
        elif arg in ['false', '0', 'no', 'n']:
            return False
        else:
            return None
    else:
        return True

def display_combinations(print_combinations):
    if print_combinations:
        print("Displaying combinations...")
    else:
        print("Not displaying combinations...")

def main():
    print_combinations = command_line_argument()

    if print_combinations is None:
        handle_error(f"Invalid argument: {sys.argv[1]}")
        print("Usage: python script_name.py [true or false]")
        return

    display_combinations(print_combinations)

    if print_combinations:
        frase = get_input()
        if not frase:
            handle_error("No input provided")
            return

        words = frase.split()
        if not words:
            handle_error("No words to reverse")
            return

        reversed_phrase = reverse_phrase(words)
        display_result(reversed_phrase)

