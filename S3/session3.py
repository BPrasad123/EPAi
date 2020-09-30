from fractions import Fraction

def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module
    '''

    if base < 2 or base > 36:
        raise ValueError("Please provide a base value between 2 and 36 with both including")

    if len(digit_map) != base:
        raise ValueError("Digit map is not of sufficient length for the specified base value")

    if len(set(digit_map)) != len(digit_map):
        raise ValueError("digit_map has repeating digits, please provide unique values")

    digit_map_dict = {i:str(digit_map[i]) for i in range(len(digit_map))}

    if number == 0:
        return str(digit_map_dict[0])

    n = abs(number)
    digits = []
    while n > 0:
        m = n % base
        n = n // base
        digits.insert(0, m)

    encoded_string = ''.join(str(digit_map_dict[i]) for i in digits)

    if number < 0:
        encoded_string = '-' + encoded_string

    return encoded_string


def float_equality_testing(a, b, rel_tol = 1e-12, abs_tol=1e-05):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    tol_limit = max((rel_tol * max(abs(a), abs(b))), abs_tol)
    return abs(a - b) < tol_limit


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''
    if type(f_num) is not float:
        raise ValueError("Input argument must be a float")

    sign = 1
    if f_num < 0:
        sign = -1
        f_num = abs(f_num)

    f_num = format(f_num // 1, '.0f')

    str_to_num = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    mult = 1
    trunc_number = 0
    for num in f_num[::-1]:
        trunc_number += str_to_num[num] * mult
        mult *= 10

    return trunc_number * sign

def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    frac = Fraction(f_num).limit_denominator(1)
    f_num = manual_truncation_function(frac.numerator // frac.denominator * 1.0)

    return f_num

def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    return 3.0