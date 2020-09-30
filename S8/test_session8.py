import pytest
import os
import inspect
import re

import session8


README_CONTENT_CHECK_FOR = [
    'test_check_with_docstring',
    'test_check_without_docstring',
    'test_check_with_less_docstring',
    'test_check_next_fibonacci_0',
    'test_check_next_fibonacci_1',
    'test_check_next_fibonacci_2',
    'test_check_next_fibonacci_3',
    'test_check_add1',
    'test_check_add2',
    'test_check_mul1',
    'test_check_div1',
    'test_check_other_add1',
    'test_check_other_add2',
    'test_check_other_mul1',
    'test_check_other_div1',
    'test_check_other2_add1',
    'test_check_other2_add2',
    'test_check_other2_mul1',
    'test_check_other2_div1',

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
    lines = inspect.getsource(session8)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_check_with_docstring():
    assert session8.docstring_check(session8.func_with_docstring) == True, "Docstring with more than 50 characters"

def test_check_without_docstring():
    assert session8.docstring_check(session8.func_without_docstring) == False, "Docstring without a doctstring at all"

def test_check_with_less_docstring():
    assert session8.docstring_check(session8.func_with_less_docstring) == False, "Docstring without a doctstring at all"

def test_check_next_fibonacci_0():
    assert session8.next_fibonacci_closure() == 0, "First fibonacci number"

def test_check_next_fibonacci_1():
    assert session8.next_fibonacci_closure() == 1, "Second fibonacci number"

def test_check_next_fibonacci_2():
    assert session8.next_fibonacci_closure() == 1, "Third fibonacci number"

def test_check_next_fibonacci_3():
    assert session8.next_fibonacci_closure() == 2, "Fourth fibonacci number"

def test_check_add1():
    _ = session8.add(1, 2)
    print(session8.func_count_dict)
    assert session8.func_count_dict == {'add': 1, 'mul': 0, 'div':0}, "Check for function counter"

def test_check_add2():
    _ = session8.add(7, 2)
    print(session8.func_count_dict)
    assert session8.func_count_dict == {'add': 2, 'mul': 0, 'div':0}, "Check for function counter"

def test_check_mul1():
    _ = session8.mul(7, 2)
    print(session8.func_count_dict)
    assert session8.func_count_dict == {'add': 2, 'mul': 1, 'div':0}, "Check for function counter"

def test_check_div1():
    _ = session8.div(1, 2)
    assert session8.func_count_dict == {'add': 2, 'mul': 1, 'div':1}, "Check for function counter"




def test_check_other_add1():
    assert session8.add2(1, 2) == (3, 'add2', 1), "Check for function counter"

def test_check_other_add2():
    assert session8.add2(7, 2) == (9, 'add2', 2), "Check for function counter"

def test_check_other_mul1():
    assert session8.mul2(7, 2) == (14, 'mul2', 1), "Check for function counter"

def test_check_other_div1():
    assert session8.div2(1, 2) == (0.5, 'div2', 1), "Check for function counter"



def test_check_other2_add1():
    assert session8.add3(1, 2) == (3, 'add2', 1), "Check for function counter"

def test_check_other2_add2():
    assert session8.add3(1, 2) == (3, 'add2', 2), "Check for function counter"

def test_check_other2_mul1():
    assert session8.mul3(7, 2) == (14, 'mul2', 1), "Check for function counter"

def test_check_other2_div1():
    assert session8.div3(1, 2) == (0.5, 'div2', 1), "Check for function counter"






