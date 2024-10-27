import sys

def search_chain(main_chain, search_chain): 
    if search_chain in main_chain: 
        return True  
    else:
        return False  

def get_user_input(prompt):
    user_input = input(prompt)
    if user_input:
        if any(char.isdigit() for char in user_input):
            print(f"Invalid input for {prompt.strip(': ')}: No numbers allowed.", file=sys.stderr)
            return None
        return user_input
    else:
        print(f"Invalid input for {prompt.strip(': ')}", file=sys.stderr)
        return None

def main():
    main_chain = get_user_input("Enter the main chain: ") 
    search_chain_text = get_user_input("Enter the chain to search for: ") 

    if main_chain is None or search_chain_text is None:
        print("Error .")
        return

    if search_chain(main_chain, search_chain_text): 
        print("The search chain is present in the main chain.") 
    else:
        print("The search chain is not present in the main chain.")

main()
