import re 
from math import lcm 

def parse_input(input_path): 
    with open(input_path, "r") as input_obj: 
        # handles the left / right instructions 
        ls = input_obj.read().split("\n") 
        
        pos_sequence = [int(ch == "R") for ch in ls[0]] 

        # build adjacency list of the nodes 
        adj_list = {} 

        for conn in ls[2:]: 
            c_parsed = re.findall(r"\w+", conn) 

            adj_list[c_parsed[0]] = c_parsed[1:]
        
        return pos_sequence, adj_list 

def get_zpath_len(start_node, end_rule, turns, adj_l): 
    path_len = 0 
    
    move_index = 0 
    current_node = start_node

    while not end_rule(current_node): 
        current_node = adj_l[current_node][turns[move_index]] 

        move_index += 1
        if move_index == len(turns): move_index = 0

        path_len += 1 
    
    return path_len 

def solve_p1(turns, adj): 
    return get_zpath_len("AAA", lambda n: n == "ZZZ", turns, adj)

def solve_p2(turns, adj): 
    path_lens = [] 

    for node in adj.keys(): 
        if node[-1] == "A": 
            path_len = get_zpath_len(node, lambda n: n[-1] == "Z", turns, adj) 
            path_lens.append(path_len) 

    return lcm(*path_lens)

turns, adj = parse_input("./Input/Day8.txt") 
print("Part 1 Solution:", solve_p1(turns, adj)) 
print("Part 2 Solution:", solve_p2(turns, adj)) 
