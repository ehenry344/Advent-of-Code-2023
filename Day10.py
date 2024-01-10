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

def get_max_pipe_dist(pipe_map):     # find the starting point 
    pos_map = [[0 for i in range(len(pipe_map))] for x in range(len(pipe_map))] 

    root_pos = None

    for i in range(len(pipe_map)): 
        for j in range(len(pipe_map[i])): 
            if pipe_map[i][j] == "S": 
                root_pos = (i, j) 

    # compute distance from point to point 
                
    
    frontier = [(root_pos, 0)]
    visited = {} 

    max_dist = 0
    max_pos = None 

    while len(frontier) != 0: 
        c_pos, c_dist = frontier.pop(0)       

        for adj_offset in pipe_neighbors[pipe_map[c_pos[0]][c_pos[1]]]: 
            next_pos = (c_pos[0] + adj_offset[0], c_pos[1] + adj_offset[1]) 

            if is_valid_pos(next_pos, len(pipe_map)) and not visited.get(next_pos, False): 
                if pipe_map[next_pos[0]][next_pos[1]] != ".": 
                    frontier.append((next_pos, c_dist+1))

                    if max_dist < c_dist + 1: 
                        max_dist = c_dist + 1
                        max_pos = next_pos 
                    
                    pos_map[next_pos[0]][next_pos[1]] = c_dist + 1

        visited[c_pos] = True 

    pos_map[root_pos[0]][root_pos[1]] = 3500 
    pos_map[max_pos[0]][max_pos[1]] = 3500 

    plt.imshow(pos_map, cmap="turbo") 
    plt.show()

    return max_dist
    
pipe_map = [list(line) for line in open("./Input/Day10.txt", "r").read().split("\n")] 

print("Part 1 Solution:", get_max_pipe_dist(pipe_map)) 
