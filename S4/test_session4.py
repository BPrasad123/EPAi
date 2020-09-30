import pytest
import random
import os
import inspect
import re
import math
from decimal import Decimal
import session4

README_CONTENT_CHECK_FOR = [
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__',
    'test_readme_exists',
    'test_readme_contents',
    'test_readme_proper_description',
    'test_readme_file_for_formatting',
    'test_indentations',
    'test_function_name_had_cap_letter',
    'test_input_values',
    'test_sum_multi_equal',
    'test_square_root',
    'test_false_case',
    'test_true_case',
    'test_add_method',
    'test_and_case',
    'test_or_case',
    'test_str_case',
    'test_repr_case',
    'test_equal_case',
    'test_float_case',
    'test_ge_case',
    'test_gt_case',
    'test_le_case',
    'test_lt_case',
    'test_invertsign_case',
    'test_multiplication_case',
    'test_bool_case',
    'test_isclose_case',
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
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_input_values():    
    with pytest.raises(ValueError) as e_info:
        q = session4.Qualean(5)

def test_sum_multi_equal():
    q = session4.Qualean(1)
    l_sum = 0
    for i in range(100):
        l_sum = q + l_sum
    r_sum = q * 100
    assert l_sum == r_sum, f"You are losing precision values"

def test_square_root():
    q = session4.Qualean(1)
    if q >= 0:
        assert q.__sqrt__() == Decimal(q.__str__()).sqrt(), f"square root error"

def test_false_case():
    q1 = session4.Qualean(0)
    assert (bool(q1) and bool(q2)) == False, f"False case failed"

def test_true_case():
    q1 = session4.Qualean(1)
    assert (bool(q1) or bool(q2)) == True, f"True case failed"

def test_add_method():    
    with pytest.raises(ValueError) as e_info:
        q = session4.Qualean(1)
        print(q + 'something')

def test_and_case():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(1)
    assert (bool(q1 and q2) in [True, False]), f"And case failed"

def test_or_case():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(1)
    assert (bool(q1 or q2) in [True, False]), f"Or case failed"

def test_str_case():
    q1 = session4.Qualean(1)
    assert (type(q1.__str__()) == str), f"Str case failed"

def test_repr_case():
    q1 = session4.Qualean(1)
    assert (type(q1.__repr__()) == str), f"Reprensation case failed"

def test_equal_case():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(1)
    assert ((q1 == q2) in [True, False]), f"Equal case failed"

def test_float_case():
    q1 = session4.Qualean(1)
    assert (type(float(q1)) == float), f"Float case failed"


def test_ge_case():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(1)
    assert ((q1 >= q2) in [True, False]), f"GE case failed"

def test_gt_case():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(1)
    assert ((q1 > q2) in [True, False]), f"GT case failed"

def test_le_case():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(1)
    assert ((q1 <= q2) in [True, False]), f"LE case failed"

def test_lt_case():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(1)
    assert ((q1 < q2) in [True, False]), f"LT case failed"


def test_invertsign_case():
    q1 = session4.Qualean(1)
    assert (q1.__invertsign__() == (q1 * -1)), f"invertsign case failed"

def test_multiplication_case():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(1)
    assert ((q1 * q2) == (q2 * q1)), f"Multiplication case failed"

def test_bool_case():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(0)
    q3 = session4.Qualean(-1)
    assert bool(q1 and q2 and q3) == False, f"Boolean case failed"

def test_isclose_case():
    sum_v = 0
    for i in set(range(1000000)):
        q = session4.Qualean(random.choice([1, 0, -1]))
        sum_v = q + sum_v
    assert math.isclose(sum_v, 0, abs_tol=1000), f"Not close enough"