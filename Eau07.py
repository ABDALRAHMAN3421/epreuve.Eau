import sys

def process_word():
    word = input("Enter a word: ")

    if word.isdigit():
        print("error")
    elif not word:
        print("Error: No input provided", file=sys.stderr)
    else:
        print(word.title())

def main():
    process_word()


main()
