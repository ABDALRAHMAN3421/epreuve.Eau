import sys

def sort_elements(elements):
    if not elements:
        print("Error: No elements to sort.")
        return None
    new_elements = elements.split()
    new_elements = sorted(new_elements)
    return new_elements

def main():
    if len(sys.argv) > 1:
        elements = ' '.join(sys.argv[1:])
        sorted_elements = sort_elements(elements)
        if sorted_elements is not None:
            print("Elements sorted by ASCII order: ")
            print(sorted_elements)
    else:
        while True:
            elements = input("Enter a phrase or a sequence of characters (or type 'exit' to quit): ")
            
            if elements.lower() == 'exit':
                print("Exiting program.")
                break
            
            sorted_elements = sort_elements(elements)
            if sorted_elements is not None:
                print("Elements sorted by ASCII order: ")
                print(sorted_elements)

    main()
