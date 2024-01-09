

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

def print_pos_map(pos_map): 
    for row in pos_map: 
        print(*row)

def get_max_pipe_dist(pipe_map): 
    pos_map = [x[:] for x in pipe_map]
    # find the starting point 
    root_pos = None

    for i in range(len(pipe_map)): 
        for j in range(len(pipe_map[i])): 
            if pipe_map[i][j] == "S": 
                root_pos = (i, j) 

    frontier = [(root_pos, 0)]
    visited = [] 

    max_dist = 0

    while len(frontier) != 0: 
        c_pos, c_dist = frontier.pop(0)         

        for adj_offset in pipe_neighbors[pipe_map[c_pos[0]][c_pos[1]]]: 
            next_pos = (c_pos[0] + adj_offset[0], c_pos[1] + adj_offset[1]) 

            if is_valid_pos(next_pos, len(pipe_map)) and next_pos not in visited: 
                if pipe_map[next_pos[0]][next_pos[1]] != ".": 
                    frontier.append((next_pos, c_dist+1)) 
                    max_dist = max(max_dist, c_dist+1) 

        pos_map[c_pos[0]][c_pos[1]] = c_dist 
        visited.append(c_pos)         

    print_pos_map(pos_map) 
    return max_dist
    
pipe_map = [list(line) for line in open("./Input/Day10.txt", "r").read().split("\n")] 

print("Part 1 Solution:", get_max_pipe_dist(pipe_map)) 
