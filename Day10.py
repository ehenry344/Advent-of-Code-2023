import matplotlib.pyplot as plt

pipe_neighbors = {
    "|": [(-1, 0), (1, 0)], 
    "-": [(0, -1), (0, 1)], 
    "L": [(-1, 0), (0, 1)], 
    "J": [(-1, 0), (0, -1)], 
    "7": [(1, 0), (0, -1)], 
    "F": [(1, 0), (0, 1)], 
    "S": [(-1, 0), (1, 0), (0, -1), (0, 1)]
}

def is_valid_pos(pos, map_size):
    return 0 <= pos[0] < map_size and 0 <= pos[1] < map_size 

def build_dist_map(input_map): 
    dist_map = [[0 for j in range(len(input_map))] for i in range(len(input_map))]

    for i in range(len(input_map)): 
        for j in range(len(input_map)): 
            if input_map[i][j] == "S": root_pos = (i, j) 

    frontier = [(root_pos, 0)] 
    visited = {} 

    steps = 0 

    while len(frontier) != 0: 
        c_pos, c_dist = frontier.pop(0) 

        if c_dist >= steps and not visited.get(c_pos, False): 
            steps += 1

            visited[c_pos] = True 
            
            dist_map[c_pos[0]][c_pos[1]] = c_dist

            for n_offset in pipe_neighbors[input_map[c_pos[0]][c_pos[1]]]: 
                n_pos = (c_pos[0] + n_offset[0], c_pos[1] + n_offset[1]) 

                if is_valid_pos(n_pos, len(input_map)) and input_map[n_pos[0]][n_pos[1]] != ".": 
                    frontier.append((n_pos, steps)) 

    return dist_map, steps


pipe_map = [list(line) for line in open("./Input/Day10.txt", "r").read().split("\n")] 

distances, steps = build_dist_map(pipe_map)
print(steps//2) 


    
