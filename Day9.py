def parse_input(input_path): 
    with open(input_path, "r") as input_data: 
        return_list = [] 

        for line in input_data.read().split("\n"): 
            return_list.append([int(n) for n in line.split()]) 

        return return_list 
    
def extrap_end(diff_table, ex_step, prev_value): 
    if ex_step == 0: 
        return diff_table[0][-1] + prev_value 
    
    return extrap_end(diff_table, ex_step-1, prev_value + diff_table[ex_step][-1]) 

def extrap_front(diff_table, ex_step, prev_value): 
    if ex_step == 0: 
        return diff_table[0][0] - prev_value
    
    return extrap_front(diff_table, ex_step-1, diff_table[ex_step][0] - prev_value)
    
def solve(sensor_data): 
    back_extrap, front_extrap = 0, 0 

    for r in sensor_data: 
        diff_table = [r] 
        is_constant = False 

        while not is_constant: 
            is_constant = True # start by assuming it is constant and check if it later changes 

            c_table = diff_table[-1]
            new_table = [c_table[1]-c_table[0]] #prime it with first value

            for i in range(2, len(c_table)): 
                step_diff = c_table[i] - c_table[i-1] 

                if is_constant and new_table[-1] != step_diff: 
                    is_constant = False 

                new_table.append(step_diff) 

            diff_table.append(new_table) 
        
        back_extrap += extrap_end(diff_table, len(diff_table)-1, 0) 
        front_extrap += extrap_front(diff_table, len(diff_table)-1, 0) 


    return back_extrap, front_extrap 

readings = parse_input("./Input/Day9.txt") 

p1_extrap, p2_extrap = solve(readings) 
print("Part 1 Solution:", p1_extrap) 
print("Part 2 Solution:", p2_extrap) 
