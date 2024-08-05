import sys

def reverse_phrase(words):
    return ' '.join(words[::-1])

def get_input():
    if len(sys.argv) > 1:
        return ' '.join(sys.argv[1:])
    else:
        return input("Enter a phrase please: ")

def display_result(phrase, reverse=True):
    print("Reversed Phrase:" if reverse else "Original Phrase:")
    words = phrase.split()
    if reverse:
        words = words[::-1]
    for word in words:
        print(word)

def handle_error(e):
    print(f"Error: {e}")

def main():
    frase = get_input()
    if not frase:
        handle_error("No input provided.")
        return
    
    reversed_phrase = reverse_phrase(frase.split())
    display_result(reversed_phrase, reverse=True)


    main()

