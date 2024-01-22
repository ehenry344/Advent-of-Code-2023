# shortest path between each pair of galaxies 
import math

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

    # distance between pairs of galaxies

    for row in range(len(space_map)): 
        for col in range(len(space_map[0])): 
            if space_map[row][col] == "#": 
                galaxies.append((row, col)) 

    return galaxies 

def build_pairs(galaxies): 
    galaxy_pairs = {}

    for g in galaxies: 
        galaxy_pairs[g] = [] 

        for elem in galaxies: 
            if elem == g: continue 

            elem_pairs = galaxy_pairs.get(elem, None) 

            if not elem_pairs or g not in elem_pairs: 
                galaxy_pairs[g].append(elem) 
    
    return galaxy_pairs

def euclidean_dist(p1, p2): 
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[0])**2)

def get_min_node(queue, dist): 
    min_node = 0

    for i in range(1, len(queue)): 
        if dist[queue[i]] < dist[queue[min_node]]: 
            min_node = i 
    
    return min_node

def get_neighbors(pos, dims): 
    if pos[0]-1 >= 0:
        yield (pos[0]-1, pos[1])
    if pos[0]+1 < dims[0]: 
        yield (pos[0]+1, pos[1])
    if pos[1]-1 >= 0: 
        yield (pos[0], pos[1]-1) 
    if pos[1]+1 < dims[1]: 
        yield (pos[0], pos[1]+1) 


def pair_dijkstra(input_map, pairs): 
    paths = []

    map_dims = (len(input_map), len(input_map[0])) 
    print(pairs.keys()) 
    start_pos = list(pairs.keys())[0] 
    dist = {start_pos: 0} 
    prev = {} 

    pos_queue = []


    for r in range(map_dims[0]): 
        for c in range(map_dims[1]): 
            dist[(r, c)] = 9999 
            prev[(r, c)] = None 

            pos_queue.append((r, c)) 

    while len(pos_queue) != 0: 
        min_node = pos_queue.pop(get_min_node(pos_queue, dist))
        print(min_node) 

        for neighbor in get_neighbors(min_node, map_dims): 
            print(neighbor) 
            print(neighbor) 
            if dist[neighbor] > dist[min_node] + 1: 
                print("Here") 
                dist[neighbor] = dist[min_node] + 1 
                prev[neighbor] = min_node
        
    print(dist) 




def render_input(to_render): 
    for row in to_render: 
        row_str = "" 

        for col in row: 
            row_str += col





def main(): 
    input_list = parse_input("./Input/Day11.txt") 
    galaxy_pairs = build_pairs(get_galaxies(input_list)) 

    pair_dijkstra(input_list, galaxy_pairs) 
    
main()
