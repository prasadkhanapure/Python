def number_pattern(n):
    
    if not isinstance(n, int):
        return "Argument must be an integer value."
    
    if n < 1:
        return "Argument must be an integer greater than 0."

    string = "";
    for number in range(1, n + 1):
        string += str(number) + " "
        
    print(string)
    return string.strip()

    # Alternative Method:
    numbers = []
    for number in range(1, n + 1):  
        numbers.append(str(number))

    print(numbers)
    return "".join(numbers)

number_pattern(4)