def display_combinations():
    combinations = [] 
    for i in range(100):  
        for j in range(i + 1, 100):  
            
            if i < 10:
                first_num = "0" + str(i)  
            else:
                first_num = str(i)
                
            if j < 10:
                second_num = "0" + str(j)  
            else:
                second_num = str(j)
                
            combination = first_num + " " + second_num
            combinations.append(combination) 
                                                                                                                                    
    result = ""
    for index in range(len(combinations)):
        result += combinations[index]
        if index < len(combinations) - 1:  
            result += ", "
    
    print(result)

display_combinations()

