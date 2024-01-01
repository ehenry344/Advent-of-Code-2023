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

def lt_hand(c1, c2)->bool: 
    for i in range(0, len(c1)): 
        c1_value = card_value(c1[i]) 
        c2_value = card_value(c2[i]) 

        if c1_value != c2_value: 
            return c1_value < c2_value 
        
    return False 

def classify_hand(hand: str)->int: 
    c_hist = {} 
    max_char = None 

    for ch in hand: 
        c_hist[ch] = c_hist.get(ch, 0) + 1 
        
        if max_char == None or c_hist[max_char] < c_hist[ch]: 
            max_char = ch

    hist_len = len(c_hist) 

    # edge cases 
    if hist_len == 1: 
        return 6 
    elif hist_len == 4: 
        return 1 
    elif hist_len == 5: 
        return 0 
    
    return c_hist[max_char] + (3 - hist_len)


def optimize_hand(hand_str: str)->int: 
    char_histogram = {} 
    max_char = None

    for c in hand_str: 
        char_histogram[c] = char_histogram.get(c, 0) + 1
        
        if c != 'J': 
            if max_char == None or char_histogram[max_char] < char_histogram[c]: 
                max_char = c 

    if max_char == None: 
        return 6 
    else: 
        return classify_hand(hand_str.replace('J', max_char)) 

def build_hand_groups(hands, j_rule=False): 
    hand_groups = [[] for i in range(0, 7)] 

    if j_rule: 
        card_values['J'] = -1 
    else: 
        card_values['J'] = 11

    for h in hands: 
        h_type = j_rule and optimize_hand(h) or classify_hand(h) 
        h_grp = hand_groups[h_type] 

        ins_pos = 0 

        while ins_pos != len(h_grp) and not lt_hand(h, h_grp[ins_pos]): 
            ins_pos += 1
        
        h_grp.insert(ins_pos, h) 
    
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
    
def solve(hands, bids, joker_rule=False): 
    hand_product = 0 
    rank = 1 

    h_groups = build_hand_groups(hands, joker_rule) 

    for hand_group in h_groups: 
        for hand in hand_group: 
            hand_product += bids[hand] * rank
            rank += 1 
    
    return hand_product


hands, bids = parse_input("./Input/Day7.txt")

print("Part 1 Solution:", solve(hands, bids, False)) 
print("Part 2 Solution:", solve(hands, bids, True)) 

