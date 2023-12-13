import re as regex 

def parse_input(file_path): 
    int_list = []
    symbol_list = []

    with open(file_path, "r") as input_data: 
        for line_num, line in enumerate(input_data.read().split("\n")):
            for n_match in regex.finditer(r'(\d+)|([^.])', line):
                match_v = n_match.group(0) 
                match_tup = (line_num, match_v, n_match.span())

                if match_v.isdigit():  
                    int_list.append(match_tup)
                else: 
                    symbol_list.append(match_tup) 

    return int_list, symbol_list


def solve(nums, symbols): 
    part_sum = 0 
    gear_sum = 0

    pair_lookup = {} 

    for symbol in symbols: 
        for num in nums: 
            if abs(symbol[0] - num[0]) <= 1:
                if abs(symbol[2][0] - num[2][0]) <= 1 or abs(symbol[2][1] - num[2][1]) <= 1: 
                    part_sum += int(num[1]) 
                    
                    found_symbol = pair_lookup.get(id(symbol)) 

                    if found_symbol:
                        gear_sum += int(found_symbol[1]) * int(num[1])
                    else: 
                        pair_lookup[id(symbol)] = num
                    
    return part_sum, gear_sum

parsed = parse_input("./Input/Day3.txt")
part, gear = solve(*parsed) 

print("Part 1 Solution:", part)
print("Part 2 Solution:", gear) 