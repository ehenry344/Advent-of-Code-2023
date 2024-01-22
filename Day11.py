# shortest path between each pair of galaxies 

def parse_input(input_path): 
    with open(input_path, "r") as input_stream: 
        space_map = [] 

        for line in input_stream.read().split("\n"): 
            space_map.append(list(line))

        # deal with row / column expansion             
        r_index = 0
        while r_index < len(space_map): 
            if len(set(space_map[r_index])) == 1: 
                space_map.insert(r_index+1, space_map[r_index].copy())
                r_index += 2
            else: 
                r_index += 1

        c_index = 0 
        while c_index < len(space_map[0]): 
            is_homogenous = True

            for i in range(len(space_map)): 
                if space_map[i][c_index] != ".": 
                    is_homogenous = False
            
            if is_homogenous: 
                for i in range(len(space_map)): 
                    space_map[i][c_index+1:c_index+1] = ["."] 

            c_index += 2 ** is_homogenous
    
        return space_map 
    
def get_galaxies(space_map): 
    galaxies = [] 

    for row in range(len(space_map)): 
        for col in range(len(space_map[0])): 
            if space_map[row][col] == "#": 
                galaxies.append((row, col)) 

    return galaxies 

def render_input(to_render): 
    for row in to_render: 
        row_str = "" 

        for col in row: 
            row_str += col
        
        print(row_str) 




def main(): 
    input_list = parse_input("./Input/Day11.txt") 
    galaxy_list = get_galaxies(input_list) 

    print(galaxy_list) 
main()
