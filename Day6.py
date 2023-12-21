import re

RACE_TIME = 0
RACE_DIST = 1 

def parse_input(file_path): 
    with open(file_path, "r") as input_data: 
        time_data = map(int, re.findall("\d+", input_data.readline())) 
        mag_data = map(int, re.findall("\d+", input_data.readline())) 

        return list(zip(time_data, mag_data)) 
    
def num_routes(race): 
    mean_v = race[RACE_DIST] // race[RACE_TIME] 
    record_routes = 0 

    for i in range(mean_v+1, race[RACE_TIME]): 
        dist = (i*race[RACE_TIME]) - (i**2) 
        if dist > race[RACE_DIST]: 
            record_routes += 1 
    
    return record_routes
    
def solve_p1(races): 
    win_prod = 1

    for race in races: 
        win_prod *= num_routes(race) 

    return win_prod 

def solve_p2(races): # brute force kinda slow, but works 
    race_time, race_dist = "", "" 

    for r in races: 
        race_time += str(r[RACE_TIME]) 
        race_dist += str(r[RACE_DIST]) 

    race_time = int(race_time) 
    race_dist = int(race_dist) 

    return num_routes((race_time, race_dist))  

    
race_list = parse_input("./Input/Day6.txt") 

print("Part 1 Solution:", solve_p1(race_list)) 
print("Part 2 Solution:", solve_p2(race_list)) 
