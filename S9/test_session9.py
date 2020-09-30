import pytest
import os
import inspect
import re
import time

import session9


README_CONTENT_CHECK_FOR = [
    'test_check_with_docstring',
    'test_oadd_oddrun',
    'test_mul',
    'test_authenticate',
    'test_fib_reduce',
    'test_get_access',
    'test_htmlize_complex_numbers',
    'oddrun',
    'oadd',
    'logged',
    'mul',
    'set_password',
    'authenticate',
    'timed',
    'fib_reduce',
    'set_profiles',
    'grant_access',
    'get_access',
    'htmlize',
    'htmlize_complex_numbers',
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
    lines = inspect.getsource(session9)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_check_with_docstring():
    assert len(session9.oddrun.__doc__) > 0, "Docstring exists"
    assert len(session9.add.__doc__) > 0, "Docstring exists"
    assert len(session9.logged.__doc__) > 0, "Docstring exists"
    assert len(session9.set_password.__doc__) > 0, "Docstring exists"
    assert len(session9.authenticate.__doc__) > 0, "Docstring exists"
    assert len(session9.timed.__doc__) > 0, "Docstring exists"
    assert len(session9.set_profiles.__doc__) > 0, "Docstring exists"
    assert len(session9.grant_access.__doc__) > 0, "Docstring exists"
    
def test_oadd_oddrun():
    r = []
    for i in range(5):
        r.append(session9.oadd(1, 2))
        time.sleep(1.5)
    if None in r:
        r.remove(None)
    assert len(r) < 5, "Check for only odd second runs"

def test_mul():
    assert session9.mul(2,3,4) == 24, "Check mul function if returning correct result"

def test_authenticate():    
    with pytest.raises(ValueError) as e_info:
        _ = session9.authenticate(session9.add, session9.current_password, 'pasasdcasdc'), 'incorrect login'

def test_fib_reduce():
    assert session9.fib_reduce(4) == 5, "Check fib_reduce function"

def test_get_access():
    assert session9.get_access('high') == ['a', 'b', 'c', 'd'], "Check get_access function"

def test_htmlize_complex_numbers():
    assert session9.htmlize_complex_numbers(1+2j) == '(1+2j)(<i>(1+2j)</i>)', "Check htmlize_complex_numbers function"

