import re 

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
    
def get_zpath(start_node, turns, adj_list, end_rule): 
    move_index = 0
    path = [start_node] 

    while not end_rule(path[-1]): 
        path.append(adj_list[path[-1]][turns[move_index]]) 

        move_index += 1 

        if move_index == len(turns): 
            move_index = 0 

    return path

def solve_p1(turns, adj): 
    return len(get_zpath("AAA", turns, adj, lambda n: n == "ZZZ"))-1

def solve_p2(turns, adj): 
    path_lens = [] 

    for node in adj.keys(): 
        if node[-1] == "A": 
            z_path = get_zpath(node, turns, adj, lambda n: n[-1] == "Z")

            path_lens.append(len(z_path)-1) 

    min_path = min(path_lens)-1
    c_product = 1
    print(path_lens) 
    print(min_path) 
    for p in path_lens: 
        c_product *= (p - min_path) 

    return min_path + sum(path_lens) 


turns, adj = parse_input("./Input/Day8.txt") 
# current answer : too low 
#print("Part 1 Solution:", solve_p1(turns, adj)) 
print("Part 2 Solution:", solve_p2(turns, adj)) 
