import sys

def generate_combination(enable_combination_generation):
    if not enable_combination_generation:
        print("Combination generation is disabled.", file=sys.stderr)
        return None

    combination = []
    for i in range(1, 11): 
        for j in range(i, 11):
            for k in range(j, 11): 
                combination.append((i, j, k))

    if not combination:
        print("Error in generating combination", file=sys.stderr)
        return None

    return combination


def analyze_combination(combination):
    if combination is None:
        print("Error: No combination to analyze", file=sys.stderr)
        return None

    count = len(combination)
    return count


def resolve_problem(count):
    if count is None:
        print("Error: No count to resolve", file=sys.stderr)
        return None

    threshold = 500
    if count > threshold:
        resolution = "The number of combinations exceeds the threshold."
    else:
        resolution = "The number of combinations does not exceed the threshold."

    return resolution


def display_result(result, combination=None):
    if result is None:
        print("Error: No result to display", file=sys.stderr)
        return

    print(result)
    
    
    if combination:
        print("Combinations:")
        for comb in combination:
            print(comb)

def main():
    enable_combination_generation = True  


    combination = generate_combination(enable_combination_generation)
    if combination is None:
        return

    
    count = analyze_combination(combination)
    if count is None:
        return

   
    result = resolve_problem(count)
    if result is None:
        return

   
    display_result(result, combination)

