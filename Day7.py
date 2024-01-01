card_values = {
    'A': 14, 
    'K': 13, 
    'Q': 12, 
    'J': 11, 
    'T': 10
}

def card_value(card): 
    if card.isdecimal(): 
        return int(card) 
    
    return card_values[card] 

def lt_hand(c1, c2, joker_rule)->bool: 
    if joker_rule: 
        card_values['J'] = -1

    for i in range(0, len(c1)): 
        c1_value = card_value(c1[i]) 
        c2_value = card_value(c2[i]) 

        if c1_value != c2_value: 
            return c1_value < c2_value 
        
    return False 
        
def classify_hand(hand_str: str)->int: # a cleaner hand classifier??? 
    char_histogram = {} 

    for c in hand_str: 
        char_histogram[c] = char_histogram.get(c, 0) + 1
        
    hist_size = len(char_histogram) 

    if hist_size == 1: 
        return 6 
    elif hist_size == 5: 
        return 0

    h_values = char_histogram.values() 

    if hist_size == 2: 
        if 4 in h_values: 
            return 5
        else: 
            return 4
        
    elif hist_size == 3: 
        if 3 in h_values: 
            return 3
        else:
            return 2
     
    return 5-hist_size

def build_hand_groups(hands, j_rule=False): 
    hand_groups = [[] for i in range(0, 7)] 

    for h in hands: 
        h_grp = hand_groups[classify_hand(h)] 

        ins_pos = 0 

        while ins_pos != len(h_grp) and not lt_hand(h, h_grp[ins_pos], j_rule): 
            insert_at += 1
        
        h_grp.insert(insert_at, h) 
    
    return hand_groups

        
def parse_input(file_path): 
    with open(file_path, "r") as input_data: 
        hands = [] 
        bid_lookup = {} 

        for line in input_data.read().split("\n"): 
            line = line.split() 

            hand = line[0] 

            bid_lookup[hand] = int(line[1]) 
            hands.append(hand) 
        
        return hands, bid_lookup 


def solve_p1(hands, bids): 
    hand_product = 0
    rank = 1

    h_groups = build_hand_groups(hands, False) 

    for hand_group in hands: 
        for hand in hand_group: 
            hand_product += bids[hand] * rank 
            rank+=1 

    return hand_product 

def solve_p2(hands, bids): 
    pass
    
hands, bids = parse_input("./Input/Day7.txt")

print("Part 1 Solution:", solve_p1(h_groups, bids)) 
