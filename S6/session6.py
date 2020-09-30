import random
from collections import Counter

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

deck_first = list(map(lambda x: x[0] + '_' + x[1], list(zip(vals*len(suits), suits*len(vals)))))

def create_deck(vals: 'a list of all values', suits: 'a list of suits') -> '52 unique cards':
    '''Function without lambda, map and zip: Create combinations of vals abd suits to create 52 unique cards'''
    deck_alt = []
    for v in vals:
        for s in suits:
            d = v+'_'+s
            deck_alt.append(d)
    return deck_alt

deck_alt = create_deck(vals, suits)
card_value = {vals[i]:2+i for i in range(len(vals))}

def card_split(hand: 'a list of cards in a hand') -> 'returns values and suits in separate lists':
    '''Split the card to create vals and suits for further processing'''
    hand_vals = [card.split('_')[0] for card in hand]
    hand_suits = [card.split('_')[1] for card in hand]
    return hand_vals, hand_suits

def royal_flush(hand_vals: 'values of a hand', hand_suits: 'suits of a hand') -> 'return boolean for if hand is royal flush':
    '''A, K, Q, J, 10, all the same suit.'''
    if len(hand_vals) != 5:
        raise ValueError("Royal Flush is applicable to 5 cards hand only")
    RF = False
    if len(set(hand_suits)) == 1:
        if set(hand_vals) == set(['10', 'jack', 'queen', 'king', 'ace']):
            RF = True
    return RF

def straight_flush(hand_vals: 'list of values of cards', hand_suits: 'list of suits of cards') -> 'boolean':
    '''All cards in a sequence, all in the same suit.'''
    SF = False
    if len(set(hand_suits)) == 1:
        temp = sorted([card_value[h] for h in hand_vals])
        str_temp = ''.join([str(c) for c in temp])
        str_temp_ace = '1' + str_temp[:-2]
        if (str_temp in '234567891011121314') or (str_temp_ace in '12345678910111213'):
            SF = True
    return SF

def four_of_a_kind(hand_vals: 'list of values of cards') -> 'boolean':
    '''All four cards of the same rank. Applible for hands with 4 or 5 cards only.'''
    if len(hand_vals) < 4:
        raise ValueError("Four of a Kind is valid for a hand of 4 or 5 cards only")
    FK = False
    dict_temp = dict(Counter(hand_vals))
    if 4 in dict_temp.values():
        FK = True
    return FK

def full_house(hand_vals: 'list of values of cards', hand_suits: 'list of suits of cards') -> 'boolean':
    '''Three of a kind with a pair. Applicable only for hands with 5 cards.'''
    if len(hand_vals) != 5:
        raise ValueError("Full House is applicable to 5 cards hand only")
    FH = False
    dict_temp = dict(Counter(hand_vals))
    if set(dict_temp.values()) == {3, 2}:
        FH = True
    return FH

def flush(hand_vals: 'list of values of cards', hand_suits: 'list of suits of cards') -> 'boolean':
    '''All cards of the same suit, but not in a sequence.'''
    FL = False
    if len(set(hand_suits)) == 1:
        temp = sorted([card_value[h] for h in hand_vals])
        str_temp = ''.join([str(c) for c in temp])
        str_temp_ace = '1' + str_temp[:-2]
        if (str_temp in '234567891011121314') or (str_temp_ace in '12345678910111213'):
            FL = False
        else:
            FL = True
    return FL

def straight(hand_vals: 'list of values of cards', hand_suits: 'list of suits of cards') -> 'returns boolean':
    '''All cards in a sequence, but not of the same suit.'''
    ST = False
    if len(set(hand_suits)) != 1:
        temp = sorted([card_value[h] for h in hand_vals])
        str_temp = ''.join([str(c) for c in temp])
        str_temp_ace = '1' + str_temp[:-2]
        if (str_temp in '234567891011121314') or (str_temp_ace in '12345678910111213'):
            ST = True
    return ST

def three_of_a_kind(hand_vals: 'list of values of cards') -> 'return boolean':
    '''Three cards of the same rank.'''
    TK = False
    dict_temp = dict(Counter(hand_vals))
    if 3 in dict_temp.values():
        TK = True
    return TK

def two_pair(hand_vals: 'list of values of cards') -> 'boolean if two pair satisfied':
    '''Two different pairs.'''
    if len(hand_vals) < 4:
        raise ValueError("Two Pair is valid for a hand of 4 or 5 cards only")
    TP = False
    dict_temp = dict(Counter(hand_vals))
    dict_temp = dict(Counter(dict_temp.values()))
    if (2 in dict_temp.keys()) and (dict_temp[2] == 2):
        TP = True
    return TP

def one_pair(hand_vals: 'list of values of cards') -> 'boolean if one pair satisfied':
    '''Two cards of the same rank.'''
    OP = False
    dict_temp = dict(Counter(hand_vals))
    dict_temp = dict(Counter(dict_temp.values()))
    if (2 in dict_temp.keys()) and (dict_temp[2] == 1):
        OP = True
    return OP

def high_card(hand: 'list of cards in hand') -> 'returns number(int) of highest card':
    '''When you haven't made any of the hands above, the highest card plays.
    In the example below, the jack plays as the highest card.'''
    hand_vals, hand_suits = card_split(hand)
    hand_vals_new = [card_value[h] for h in hand_vals]
    return max(hand_vals_new)

def get_highest_rank(hand: 'list of cards in hand') -> 'returns highest rank of hand':
    '''
    Get the highest rank for a hand except High Card
    Rules vary depending upon the number of cards in a hand as follows:

    For 5-card poker ranks in order (highest to lowest)
    Royal flush
    Straight flush
    Four of a kind
    Full house
    Flush
    Straight
    Three of a kind
    Two pair
    Pair
    High Card

    For 4-card poker ranks in order (highest to lowest)
    Four of a kind
    Straight flush
    Three of a kind
    Flush
    Straight
    Two pair
    One pair
    High card

    For 3-card poker ranks in order (highest to lowest)
    Straight flush
    Three of a kind
    Straight
    Flush
    Pair
    High card
    '''
    card_count = len(hand)
    hand_vals, hand_suits = card_split(hand)
    if card_count not in [3, 4, 5]:
        raise ValueError("Permitted size of hand is 3 or 4 or 5")

    if card_count == 5:
        if royal_flush(hand_vals, hand_suits):
            return 9
        elif straight_flush(hand_vals, hand_suits):
            return 8
        elif four_of_a_kind(hand_vals):
            return 7
        elif full_house(hand_vals, hand_suits):
            return 6
        elif flush(hand_vals, hand_suits):
            return 5
        elif straight(hand_vals, hand_suits):
            return 4
        elif three_of_a_kind(hand_vals):
            return 3
        elif two_pair(hand_vals):
            return 2
        elif one_pair(hand_vals):
            return 1
        else:
            return 0

    if card_count == 4:
        if four_of_a_kind(hand_vals):
            return 7
        elif straight_flush(hand_vals, hand_suits):
            return 6
        elif three_of_a_kind(hand_vals):
            return 5
        elif flush(hand_vals, hand_suits):
            return 4
        elif straight(hand_vals, hand_suits):
            return 3
        elif two_pair(hand_vals):
            return 2
        elif one_pair(hand_vals):
            return 1
        else:
            return 0

    if card_count == 3:
        if straight_flush(hand_vals, hand_suits):
            return 5
        elif three_of_a_kind(hand_vals):
            return 4
        elif straight(hand_vals, hand_suits):
            return 3
        elif flush(hand_vals, hand_suits):
            return 2
        elif one_pair(hand_vals):
            return 1
        else:
            return 0

def decide_winner(hand1: 'list of hand1 cards', hand2: 'list of hand2 cards') -> 'decides which hand wins':
    '''Given two hands find out which one is the winner'''
    rank1 = get_highest_rank(hand1)
    rank2 = get_highest_rank(hand2)
    if rank1 and rank2:
        if rank1 > rank2:
            print(f'Winner is {hand1}')
            return hand1
        elif rank1 == rank2:
            winner = random.choice((hand1, hand2))
            print(f"Tie between hand1 and hand2 with score {rank1} so random winner is {winner}")
            return winner
        else:
            print(f'Winner is {hand2}')
            return hand2
    elif (rank1 == 0) and (rank1 == 0):
        rank1 = high_card(hand1)
        rank2 = high_card(hand2)
        if rank1 > rank2:
            print(f'Winner is {hand1}')
            return hand1
        elif rank1 == rank2:
            winner = random.choice((hand1, hand2))
            print(f"Tie between hand1 and hand2 with score {rank1} so random winner is {winner}")
            return winner
        else:
            print(f'Winner is {hand2}')
            return hand2
    else:
        if rank1 > 0:
            print(f'Winner is {hand1}')
            return hand1
        else:
            print(f'Winner is {hand2}')
            return hand2

def get_hands_and_winner(count: 'a number specifying number of cards in hand', solo=False) -> 'returns one or two hands':
    '''Depending upon the number of requested cards create two sets of hands'''
    if (count < 3) or (count > 5):
        raise ValueError("Permitted number of cards in each hand is 3 or 4 or 5.")
    deck = sorted(deck_first, key=lambda x: random.random())
    hands = [deck[i] for i in random.sample(range(len(deck)), count*2)]
    hand1 = hands[:count]
    hand2 = hands[count:]
    print(f'hand1: {hand1}')
    print(f'hand2: {hand2}')
    if solo:
        return hand1, hand2
    else:
        winner = decide_winner(hand1, hand2)
        return winner

count = 4
_ = get_hands_and_winner(count)