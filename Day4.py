import re 

def parse_cards(file_path): 
    with open(file_path, "r") as input_data: 
        card_list = [] 

        for line in input_data.read().split('\n'): 
            split_line = line.split('|') 

            win_nums = set(re.findall(r'\d+', split_line[0])[1::]) 
            found_nums = set(re.findall(r'\d+', split_line[1]))

            card_list.append((win_nums, found_nums)) 
        
        return card_list 

def get_match_list(cards): 
    return [len(c[0] & c[1]) for c in cards] 

def solve_p1(match_list): 
    point_sum = 0 

    for m in match_list: 
        if m > 0: 
            point_sum += 2**(m-1) 
    
    return point_sum 

def solve_p2(match_list): 
    num_cards = len(match_list) 
    copy_list = [1] * num_cards

    for i in range(num_cards):
        for j in range(i+1, i + match_list[i] + 1):
            copy_list[j] += copy_list[i]

    return sum(copy_list)  

cards = parse_cards("./Input/Day4.txt") 

match_list = get_match_list(cards) 

print("Part 1 Solution:", solve_p1(match_list))
print("Part 2 Solution:", solve_p2(match_list)) 