import pytest
import random
import os
import inspect
import re
import time

import session6
import session6_combinations

README_CONTENT_CHECK_FOR = [
    'vals',
    'suits',
    'deck',
    'create_deck',
    'get_hands',
    'card_split',
    'royal_flush',
    'straight_flush',
    'four_of_a_kind',
    'full_house',
    'flush',
    'straight',
    'three_of_a_kind',
    'two_pair',
    'one_pair',
    'high_card',
    'get_highest_rank',
    'decide_winner',
    'test_manual_20_combinations',
    'test_more_than_5_cards',
    'test_less_than_three_cards',
    'test_two_pair',
    'test_full_house3',
    'test_full_house4',
    'test_royal_flush3',
    'test_royal_flush4',
    'test_one_pair',
    'test_three_of_a_kind',
    'test_straight1',
    'test_straight2',
    'test_straight3',
    'test_flush',
    'test_straight_flush1',
    'test_straight_flush2',
    'test_straight_flush3',
    'test_card_split',
]

CHECK_FOR_THINGS_NOT_ALLOWED = []

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_manual_20_combinations():
    combinations = session6_combinations.list_twenty_comb
    for c in combinations:
        assert set(c[2]) == set(session6.decide_winner(c[0], c[1])), "Result not matching for combinations"

def test_more_than_5_cards():
    with pytest.raises(ValueError) as e_info:
        _ = session6.get_hands_and_winner(6)

def test_less_than_three_cards():    
    with pytest.raises(ValueError) as e_info:
        _ = session6.get_hands_and_winner(2)

def test_two_pair():    
    with pytest.raises(ValueError) as e_info:
        h1, h2 = session6.get_hands_and_winner(3, solo=True)
        h1_v, _ = session6.card_split(h1)
        _ = session6.two_pair(h1_v)

def test_full_house3():    
    with pytest.raises(ValueError) as e_info:
        h1, h2 = session6.get_hands_and_winner(3, solo=True)
        h1_v, h1_s = session6.card_split(h1)
        _ = session6.full_house(h1_v, h1_s)

def test_full_house4():    
    with pytest.raises(ValueError) as e_info:
        h1, h2 = session6.get_hands_and_winner(4, solo=True)
        h1_v, h1_s = session6.card_split(h1)
        _ = session6.full_house(h1_v, h1_s)

def test_four_of_a_kind():    
    with pytest.raises(ValueError) as e_info:
        h1, h2 = session6.get_hands_and_winner(3, solo=True)
        h1_v, _ = session6.card_split(h1)
        _ = session6.four_of_a_kind(h1_v)

def test_royal_flush3():    
    with pytest.raises(ValueError) as e_info:
        h1, h2 = session6.get_hands_and_winner(3, solo=True)
        h1_v, h1_s = session6.card_split(h1)
        _ = session6.royal_flush(h1_v, h1_s)

def test_royal_flush4():    
    with pytest.raises(ValueError) as e_info:
        h1, h2 = session6.get_hands_and_winner(4, solo=True)
        h1_v, h1_s = session6.card_split(h1)
        _ = session6.royal_flush(h1_v, h1_s)

def test_high_card():
    h1 = ['6_diamonds', 'jack_clubs', '3_hearts']
    assert session6.high_card(h1) == 11, "High card value not matching"

def test_one_pair():
    h1 = ['6_diamonds', '6_clubs', '3_hearts']
    h1_v, _ = session6.card_split(h1)
    assert session6.one_pair(h1_v) == True, "One pair test result is not matching"

def test_three_of_a_kind():
    h1 = ['6_diamonds', '6_clubs', '6_hearts', 'ace_hearts']
    h1_v, _ = session6.card_split(h1)
    assert session6.three_of_a_kind(h1_v) == True, "three_of_a_kind test result is not matching"

def test_straight1():
    h1 = ['2_diamonds', '3_clubs', '4_hearts', '5_hearts']
    h1_v, h1_s = session6.card_split(h1)
    assert session6.straight(h1_v, h1_s) == True, "straight test result is not matching"

def test_straight2():
    h1 = ['ace_clubs', '2_diamonds', '3_clubs', '4_hearts', '5_hearts']
    h1_v, h1_s = session6.card_split(h1)
    assert session6.straight(h1_v, h1_s) == True, "straight test result is not matching"

def test_straight3():
    h1 = ['ace_clubs', 'king_diamonds', 'queen_clubs', 'jack_hearts', '10_hearts']
    h1_v, h1_s = session6.card_split(h1)
    assert session6.straight(h1_v, h1_s) == True, "straight test result is not matching"

def test_flush():
    h1 = ['ace_clubs', '5_clubs', '8_clubs', '2_clubs']
    h1_v, h1_s = session6.card_split(h1)
    assert session6.flush(h1_v, h1_s) == True, "flush test result is not matching"

def test_straight_flush1():
    h1 = ['2_diamonds', '3_diamonds', '4_diamonds', '5_diamonds']
    h1_v, h1_s = session6.card_split(h1)
    assert session6.straight_flush(h1_v, h1_s) == True, "straight_flush test result is not matching"

def test_straight_flush2():
    h1 = ['ace_clubs', '2_clubs', '3_clubs', '4_clubs', '5_clubs']
    h1_v, h1_s = session6.card_split(h1)
    assert session6.straight_flush(h1_v, h1_s) == True, "straight_flush test result is not matching"

def test_straight_flush3():
    h1 = ['ace_clubs', 'king_clubs', 'queen_clubs', 'jack_clubs', '10_clubs']
    h1_v, h1_s = session6.card_split(h1)
    assert session6.straight_flush(h1_v, h1_s) == True, "straight_flush test result is not matching"

def test_card_split():
    h1 = ['ace_clubs', 'king_clubs', 'queen_clubs', 'jack_clubs', '10_clubs']
    h1_v, h1_s = session6.card_split(h1)
    assert len(h1_v) == len(h1_s), "card_split is not resulting in correct output"