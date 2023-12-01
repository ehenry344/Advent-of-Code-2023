input_path = "./Input/Day1.txt"

def digit_sum(input_data): # sums pairs of first and last integers on each line 
    calib_sum = 0 

    for line in input_data: 
        digits = list(filter(str.isdigit, line)) 

        if digits: # determine if there are digits to add
            print(digits[0] + digits[-1])
            calib_sum += int(digits[0] + digits[-1])
    
    return calib_sum 

def preprocess_digits(input_data): 
    digit_lookup = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i in range(len(input_data)): 
        for j, digit in enumerate(digit_lookup): 
            input_data[i] = input_data[i].replace(digit, digit[0] + str(j+1) + digit[-1]) # replace w/ first letter + num + last letter

    return input_data

with open("./Input/Day1.txt", "r") as calib_data: 

    calib_list = calib_data.readlines() 

    print("Part 1 Solution:", digit_sum(calib_list))
    print("Part 2 Solution:", digit_sum(preprocess_digits(calib_list))) 
