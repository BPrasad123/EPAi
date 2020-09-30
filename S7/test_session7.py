import pytest
import random
import os
import inspect
import re
import time


import session7


README_CONTENT_CHECK_FOR = [
    'check_fabinocci',
    'add_odd_even',
    'strip_vowel',
    'relu',
    'sigmoid',
    'shift_string',
    'find_profanity',
    'reduce_sum_even',
    'reduce_big_str',
    'add_third_number',
    'random_number_plates',
    'number_plates',
    'partial_number_plates',
    'test_check_fabinocci_ve',
    'test_add_odd_even_ve',
    'test_strip_vowel_ve',
    'test_relu_ve_list',
    'test_relu_ve_str',
    'test_sigmoid_ve_list',
    'test_sigmoid_ve_str',
    'test_shift_string_ve_str',
    'test_find_profanity_ve_str',
    'test_find_profanity_ve_length',
    'test_reduce_sum_even_ve_list',
    'test_reduce_sum_even_ve_str',
    'test_reduce_big_str_ve_str',
    'test_add_third_number_ve_list',
    'test_add_third_number_ve_str',
    'test_random_number_plates_ve_str',
    'test_number_plates_ve_str',
    'test_number_plates_ve_nbr',
    'test_check_fabinocci_arg',
    'test_add_odd_even_arg',
    'test_strip_vowel_arg',
    'test_relu_arg',
    'test_sigmoid_arg',
    'test_shift_string_arg',
    'test_find_profanity_arg',
    'test_reduce_sum_even_arg',
    'test_reduce_big_str_arg',
    'test_add_third_number_arg',
    'test_random_number_plates_arg',
    'test_number_plates_arg',
    'test_partial_number_plates_arg',
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
    lines = inspect.getsource(session7)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_check_fabinocci_ve():
    with pytest.raises(ValueError) as e_info:
        _ = session7.check_fabinocci('xyz')

def test_add_odd_even_ve():    
    with pytest.raises(ValueError) as e_info:
        _ = session7.add_odd_even([1,2,3], 5)

def test_strip_vowel_ve():    
    with pytest.raises(ValueError) as e_info:
        _ = session7.strip_vowel(5)

def test_relu_ve_list():    
    with pytest.raises(ValueError) as e_info:
        _ = session7.relu(5)

def test_relu_ve_str():    
    with pytest.raises(ValueError) as e_info:
        _ = session7.relu([1, 4, 7, 'd'])

def test_sigmoid_ve_list():    
    with pytest.raises(ValueError) as e_info:
        _ = session7.sigmoid(10)

def test_sigmoid_ve_str():    
    with pytest.raises(ValueError) as e_info:
        _ = session7.sigmoid([1, 2, 7, 'e'])

def test_shift_string_ve_str():    
    with pytest.raises(ValueError) as e_info:
        _ = session7.shift_string(9)

def test_find_profanity_ve_str():    
    with pytest.raises(ValueError) as e_info:
        _ = session7.find_profanity(9)

def test_find_profanity_ve_length():    
    with pytest.raises(ValueError) as e_info:
        _ = session7.find_profanity('hello, this is a test program')

def test_reduce_sum_even_ve_list():    
    with pytest.raises(ValueError) as e_info:
        _ = session7.reduce_sum_even('anything')

def test_reduce_sum_even_ve_str():    
    with pytest.raises(ValueError) as e_info:
        _ = session7.reduce_sum_even([1, 5, 4, 'a'])

def test_reduce_big_str_ve_str():    
    with pytest.raises(ValueError) as e_info:
        _ = session7.reduce_big_str([1, 5, 4])

def test_add_third_number_ve_list():    
    with pytest.raises(ValueError) as e_info:
        _ = session7.add_third_number('anything')

def test_add_third_number_ve_str():    
    with pytest.raises(ValueError) as e_info:
        _ = session7.add_third_number([1, 5, 4, 'a'])

def test_random_number_plates_ve_str():    
    with pytest.raises(ValueError) as e_info:
        _ = session7.random_number_plates('xyz')

def test_number_plates_ve_str():    
    with pytest.raises(ValueError) as e_info:
        _ = session7.number_plates('xyz')

def test_number_plates_ve_nbr():    
    with pytest.raises(ValueError) as e_info:
        _ = session7.number_plates(nl=100)

def test_check_fabinocci_arg():
    assert session7.check_fabinocci(10) == False, "Fabinocci function not working"

def test_add_odd_even_arg():
    assert session7.add_odd_even([1,2,3], [4,5,6]) == [7], "Incorrect result from odd even addition from lists"

def test_strip_vowel_arg():
    assert session7.strip_vowel('hello') == 'hll', "Incorrect result from strip_vowel"

def test_relu_arg():
    assert session7.relu([1, 4, 0, -3, 1.2]) == [1, 4, 0, 0, 1.2], "Incorrect result from relu"

def test_sigmoid_arg():
    assert session7.sigmoid([1, 4, 0, -3, 1.2]) == [0.7310585786300049, 0.9820137900379085, 0.5, 0.04742587317756678, 0.7685247834990175], "Incorrect result from sigmoid"

def test_shift_string_arg():
    assert session7.shift_string('helloz') == 'mjqqte', "Incorrect result from shift_string"

prof_pg = " t t t t t t t t t t t t t t t t t t t t t arse tDear Aditya, A good workforce of any establishment or factory is a asset and there is no harm if the HR indulge into settlement of any sort of complaint / dispute whether within or outside the premises. Moreover, I do not feel any harm if the HR even get involve into personal issues of the workforce. I remember, when I was in service, I had settled certain minor disputes within the family of workers or their friend circle, understand their problems whether relating to the school admission of their wards or medical treatment of their parents etc. etc. by advancing money either from my employer or from my own pocket. At the same time taking appropriate disciplinary action against the guilty is equally important to maintain discipline and peaceful working. In this particular case, if the employee has used abusive language through email it is on the record and HR can go through it, understand the circumstances and situations and decide further action. It is a goodwill gesture and you can win over the hearts of the workforce. They will definitely listen to your directions always. read more at: https://www.citehr.com/502881-abusive-language-used-employee-email.html"
def test_find_profanity_arg():
    assert session7.find_profanity(prof_pg) == True, "Incorrect result from find_profanity"

def test_reduce_sum_even_arg():
    assert session7.reduce_sum_even([1,2,3,4]) == 6, "Incorrect result from reduce_sum_even"

def test_reduce_big_str_arg():
    assert session7.reduce_big_str('testingyyyy') == 'y', "Incorrect result from reduce_big_str"

def test_add_third_number_arg():
    assert session7.add_third_number([1,2,3,4,5,6,7]) == 12, "Incorrect result from add_third_number"

def test_random_number_plates_arg():
    assert len(session7.random_number_plates()) == 15, "Incorrect result from random_number_plates"

def test_number_plates_arg():
    assert len(session7.number_plates()) == 15, "Incorrect result from number_plates"

def test_partial_number_plates_arg():
    assert len(session7.partial_number_plates()) == 15, "Incorrect result from partial_number_plates"
