import pytest
import random
import os
import inspect
import re
import time
from math import tan, pi

import session5

README_CONTENT_CHECK_FOR = [
    'test_readme_exists',
    'test_readme_contents',
    'test_readme_proper_description',
    'test_readme_file_for_formatting',
    'test_indentations',
    'test_function_name_had_cap_letter',
    'test_squared_power_list_more_values',
    'test_squared_power_list_no_value',
    'test_squared_power_list_str_value',
    'test_squared_power_list_extra_range',
    'test_squared_power_list_less_range',
    'test_squared_power_list_other_range',
    'test_squared_power_list_str_range',
    'test_squared_power_list_ls_check',
    'test_polygon_area_nbr_exists',
    'test_polygon_area_more_nbr',
    'test_polygon_area_nbr_str',
    'test_polygon_area_negative_nbr',
    'test_polygon_area_no_sides',
    'test_polygon_area_more_sides',
    'test_polygon_area_negative_shape',
    'test_polygon_area_shape_less2',
    'test_polygon_area_shape_more6',
    'test_temp_converter_degree_exist',
    'test_temp_converter_more_degree',
    'test_temp_converter_degree_str',
    'test_temp_converter_no_temp_unit',
    'test_temp_converter_more_temp_unit',
    'test_temp_converter_other_arg',
    'test_temp_converter_nbr_temp_unit',
    'test_temp_converter_inv_temp_unit',
    'test_speed_converter_nbr_exist',
    'test_speed_converter_more_nbr',
    'test_speed_converter_str_nbr',
    'test_speed_converter_more_arg',
    'test_speed_converter_less_arg',
    'test_speed_converter_nbr_arg',
    'test_speed_converter_inv_dist',
    'test_speed_converter_inv_time',
    'test_squared_power_list',
    'test_polygon_area',
    'test_temp_converter',
    'test_speed_converter',
    'test_print',
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
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_squared_power_list_more_values():    
    with pytest.raises(ValueError) as e_info:
        _ = session5.squared_power_list(2, 4, start=0, end=5)

def test_squared_power_list_no_value():    
    with pytest.raises(ValueError) as e_info:
        _ = session5.squared_power_list(start=0, end=5)

def test_squared_power_list_str_value():    
    with pytest.raises(ValueError) as e_info:
        _ = session5.squared_power_list('x', start=0, end=5)

def test_squared_power_list_extra_range():
    with pytest.raises(ValueError) as e_info:
        _ = session5.squared_power_list(4, start=0, end=5, extra=4)

def test_squared_power_list_less_range():
    with pytest.raises(ValueError) as e_info:
        _ = session5.squared_power_list(6, start=0)

def test_squared_power_list_other_range():
    with pytest.raises(ValueError) as e_info:
        _ = session5.squared_power_list(6, start=0, other=6)

def test_squared_power_list_str_range():
    with pytest.raises(ValueError) as e_info:
        _ = session5.squared_power_list(6, start=0, end='y')

def test_squared_power_list_ls_check():
    with pytest.raises(ValueError) as e_info:
        _ = session5.squared_power_list(6, start=4, end=1)

def test_polygon_area_nbr_exists():
    with pytest.raises(ValueError) as e_info:
        _ = session5.polygon_area(sides=4)

def test_polygon_area_more_nbr():
    with pytest.raises(ValueError) as e_info:
        _ = session5.polygon_area(16, 10, sides=4)

def test_polygon_area_nbr_str():
    with pytest.raises(ValueError) as e_info:
        _ = session5.polygon_area('x', sides=4)

def test_polygon_area_negative_nbr():
    with pytest.raises(ValueError) as e_info:
        _ = session5.polygon_area(-5, sides=4)

def test_polygon_area_no_sides():
    with pytest.raises(ValueError) as e_info:
        _ = session5.polygon_area(14)

def test_polygon_area_more_sides():
    with pytest.raises(ValueError) as e_info:
        _ = session5.polygon_area(10, sides=4, other=2)

def test_polygon_area_negative_shape():
    with pytest.raises(ValueError) as e_info:
        _ = session5.polygon_area(10, sides=-6)

def test_polygon_area_shape_less2():
    with pytest.raises(ValueError) as e_info:
        _ = session5.polygon_area(10, sides=2)

def test_polygon_area_shape_more6():
    with pytest.raises(ValueError) as e_info:
        _ = session5.polygon_area(10, sides=8)

def test_temp_converter_degree_exist():
    with pytest.raises(ValueError) as e_info:
        _ = session5.temp_converter(temp_given_in = 'f')

def test_temp_converter_more_degree():
    with pytest.raises(ValueError) as e_info:
        _ = session5.temp_converter(10, 20, temp_given_in = 'f')

def test_temp_converter_degree_str():
    with pytest.raises(ValueError) as e_info:
        _ = session5.temp_converter('x', temp_given_in = 'f')

def test_temp_converter_no_temp_unit():
    with pytest.raises(ValueError) as e_info:
        _ = session5.temp_converter(20)

def test_temp_converter_more_temp_unit():
    with pytest.raises(ValueError) as e_info:
        _ = session5.temp_converter(20, temp_given_in = 'f', other='a')

def test_temp_converter_other_arg():
    with pytest.raises(ValueError) as e_info:
        _ = session5.temp_converter(20, other='a')

def test_temp_converter_nbr_temp_unit():
    with pytest.raises(ValueError) as e_info:
        _ = session5.temp_converter(20, temp_given_in=9)

def test_temp_converter_inv_temp_unit():
    with pytest.raises(ValueError) as e_info:
        _ = session5.temp_converter(20, temp_given_in='g')

def test_speed_converter_nbr_exist():
    with pytest.raises(ValueError) as e_info:
        _ = session5.speed_converter(dist='km', time='ms')

def test_speed_converter_nbr_exist():
    with pytest.raises(ValueError) as e_info:
        _ = session5.speed_converter(dist='km', time='ms')

def test_speed_converter_more_nbr():
    with pytest.raises(ValueError) as e_info:
        _ = session5.speed_converter(10, 20, dist='km', time='ms')

def test_speed_converter_str_nbr():
    with pytest.raises(ValueError) as e_info:
        _ = session5.speed_converter('x', dist='km', time='ms')

def test_speed_converter_more_arg():
    with pytest.raises(ValueError) as e_info:
        _ = session5.speed_converter(10, dist='km', time='ms', other='x')

def test_speed_converter_less_arg():
    with pytest.raises(ValueError) as e_info:
        _ = session5.speed_converter(10, dist='km')

def test_speed_converter_nbr_arg():
    with pytest.raises(ValueError) as e_info:
        _ = session5.speed_converter(10, dist='km', time=9)

def test_speed_converter_inv_dist():
    with pytest.raises(ValueError) as e_info:
        _ = session5.speed_converter(10, dist='kmx', time='s')

def test_speed_converter_inv_time():
    with pytest.raises(ValueError) as e_info:
        _ = session5.speed_converter(10, dist='km', time='sx')

def test_squared_power_list():
    r = session5.squared_power_list(2, start=0, end=5)
    assert r == [1, 2, 4, 8, 16, 32], "Unexpected result from squared_power_list"
        
def test_polygon_area():
    r = session5.polygon_area(15, sides = 3)
    assert r == 97.42785792574938, "Unexpected result from polygon_area"

def test_temp_converter():
    r = session5.temp_converter(100, temp_given_in = 'f')
    assert r == 38, "Unexpected result from temp_converter"

def test_speed_converter():
    r = session5.speed_converter(1, dist='km', time='s')
    assert r == 3600.0, "Unexpected result from speed_converter"

def test_print():
    r = session5.time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitions=100)
    assert float(r) > 0, "Invalid execution time of print"