import re 

def parse_input(file_path):
    int_pattern = re.compile(r'\d+') 
    
    with open(file_path, "r") as input_data: 
        init_elems = int_pattern.findall(input_data.readline()) 

        init_seeds = list(map(int, init_elems)) 
    
        maps = [] 

        while new_line := input_data.readline(): 
            if new_line == "\n": 
                maps.append([]) # add empty list to add new ranges to 

            match_list = int_pattern.findall(new_line) 

            if len(match_list) > 0: 
                range_tup = tuple(map(int, match_list)) 
                # the flag at the end comes in later to check if it was used
 
                maps[len(maps) - 1].append(range_tup)

        return init_seeds, maps

def solve_p1(seeds, mappings): 
    min_location = None

    for s in seeds: 
        current_source = s

        for m in mappings: 
            for r in m: # iterate through each range in the mappings 
                if current_source >= r[1] and current_source < r[1] + r[2]: 
                    current_source = r[0] + (current_source - r[1]) 
                    break 

        if min_location == None or min_location > current_source: 
            min_location = current_source
            
    return min_location  

def gt_range(r1, r2): 
    return r1[0] + r1[2] > r2[0] + r2[2]

def solve_p2(seeds, mappings): 
    # go thru the mappings backward 
    new_mappings = [] 

    prev_reduced = []

    for m in mappings[::-1]: 
        min_range = min(m) 
        max_range = max(m) 

        reduced_ranges = [min_range, (0, max_range[1], min_range[0])]

        # now we check the reduced ranges against the list of ideals 

        for prev_range in prev_reduced: 
            pass 
                
        #ideal_inputs = [i for i in range(prev_ideal[1], prev_ideal[1] + prev_ideal[2])]
    
        #print(ideal_inputs) 

        
         
seeds, maps = parse_input("./Input/Day5.txt") 

print("Part 1 Solution:", solve_p1(seeds, maps))  

solve_p2(seeds, maps) 

# lowest possible location with default humidities: 
# 56 (humidity = 93) 
# lowest possible temperature with 
