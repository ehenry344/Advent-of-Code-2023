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

def get_max_pipe_dist(pipe_map): 

    for i in range(len(pipe_map)): #finds starting point 
        for j in range(len(pipe_map[i])): 
            if pipe_map[i][j] == "S": 
                root_pos = (i, j) 
                
    
    frontier = [(root_pos, 0)]
    visited = {} 

    max_dist = 0

    while len(frontier) != 0: 
        c_pos, c_dist = frontier.pop(0) 

        if c_dist >= max_dist and not visited.get(c_pos, False): 
            visited[c_pos] = True 

            for c_offset in pipe_neighbors[pipe_map[c_pos[0]][c_pos[1]]]: 
                check_pos = (c_pos[0] + c_offset[0], c_pos[1] + c_offset[1])

                if is_valid_pos(check_pos, len(pipe_map)): 
                    frontier.append((check_pos, c_dist+1))  

                    max_dist = max(max_dist, c_dist+1) 

    return max_dist // 2
    
pipe_map = [list(line) for line in open("./Input/Day10.txt", "r").read().split("\n")] 

print("Part 1 Solution:", get_max_pipe_dist(pipe_map)) 
