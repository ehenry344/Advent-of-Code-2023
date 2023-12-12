import re as regex 

with open("./Input/Day2.txt", "r") as input_data: 
    valid_ids = 0 
    pow_set = 0 

    for i, line in enumerate(input_data.read().strip().split("\n")):
        max_cubes = {'r': 0,'g': 0,'b': 0}

        relevant_data = regex.findall(r"(\d+) (r|g|b)", line)

        for pair in relevant_data: 
            max_cubes[pair[1]] = max(int(pair[0]), max_cubes[pair[1]]) 

        if max_cubes['r'] <= 12 and max_cubes['g'] <= 13 and max_cubes['b'] <= 14: 
            valid_ids += (i+1) 

        pow_set += max_cubes['r'] * max_cubes['g'] * max_cubes['b']

    print(valid_ids)
    print(pow_set)

