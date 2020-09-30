import math
import os
from functools import reduce, partial
import random


def fabinocci(n:'int') -> 'bool':
    '''
    Parameters
    ----------
    n : 'int'
        Takes an interger and decides if that is fabinocci number.

    Returns
    -------
    bool
        True or False for whether the number is fabinnocci number.
    '''
    fib_nbrs = [0, 1]
    while True:
        nbr = fib_nbrs[-1] + fib_nbrs[-2]
        if nbr > n:
            break
        fib_nbrs.append(nbr)
    if n in fib_nbrs:
        return True
    else:
        return False

def check_fabinocci(n:'int') -> 'bool':
    '''
    Parameters
    ----------
    n : 'int'
        Takes an interger and decides if that is fabinocci number.

    Returns
    -------
    bool
        True or False for whether the number is fabinnocci number.
    '''
    if type(n) != int:
        raise ValueError("Only integer is allowed as input")
    if n in list(filter(lambda x: fabinocci(x), range(10000))):
        return True
    else:
        return False

def add_odd_even(l1:'list', l2:'list') -> 'list':
    '''
    Parameters
    ----------
    l1 : 'list'
        First list of integers.
    l2 : 'list'
        Seecond list of integers.

    Purpose
    -------
    The function adds corrsponding elements from the lists if element from first list is even and element from second list if odd

    Raises
    ------
    ValueError
        If any of the arguments is not a list, the function raises value error.

    Returns
    -------
    list
        List with added values from both the list based on odd even condition.
    '''
    if not (type(l1) == type(l2) == list):
        raise ValueError("Both the arugments must be lists")
    return [x+y for x, y in zip(l1, l2) if (x%2 == 0) and (y%2 != 0)]

def strip_vowel(string:'str') -> 'str':
    '''
    Parameters
    ----------
    string : 'str'
        A simple string of characters is allowed.

    Raises
    ------
    ValueError
        If anything other than a string is provided, the function raises value error.

    Returns
    -------
    TYPE
        A string after removal of vowel characters.
    '''
    if type(string) != str:
        raise ValueError("Only string is allowed")
    return ''.join([s for s in string if s not in 'aeiouAEIOU'])

def relu(l:'list') -> 'list':
    '''
    Parameters
    ----------
    l : 'list'
        List of intergers or floats.

    Raises
    ------
    ValueError
        The function raises value error if anything other than list as provided as argument.
        Raises value error if any of the elements in the list is not an integer or float.

    Returns
    -------
    list
        List of intergers or floats after converting -ve number to zero.
    '''
    if type(l) != list:
        raise ValueError("Only list is allowed as arugument here")
    for i in l:
        if type(i) not in [int, float]:
            raise ValueError("The elements in the list can only be integer or float")
    return [n if n>0 else 0 for n in l]

def sigmoid(l:'list') -> 'list':
    '''
    Parameters
    ----------
    l : 'list'
        List of intergers or floats.

    Raises
    ------
    ValueError
        The function raises value error if anything other than list as provided as argument.
        Raises value error if any of the elements in the list is not an integer or float.

    Returns
    -------
    list
        List of intergers or floats after converting each number to its sigmoid value.
    '''
    if type(l) != list:
        raise ValueError("Only list is allowed as arugument here")
    for i in l:
        if type(i) not in [int, float]:
            raise ValueError("The elements in the list can only be integer or float")
    return [(1 / (1 + math.exp(-n))) for n in l]

def shift_string(string:'str') -> 'str':
    '''
    Parameters
    ----------
    string : 'str'
        Takes a string of characters. Capital letters are allowed however the function converts them to lower characters.
        Only a to z characters are considered from the given string programatically.

    Raises
    ------
    ValueError
        If anything other than a string is given then the functions raises value error.

    Returns
    -------
    TYPE
        The function shifts each letter in the string to its next 5th position and then concatenates them to return the updated string.
    '''
    if type(string) != str:
        raise ValueError("Only string is allowed")
    string = string.lower()
    ls = [((ord(s)-96) + 5)%26 for s in string if ord(s) in range(97, 123)]
    return ''.join([chr(n+96) for n in ls])

def find_profanity(pg:'str') -> 'bool':
    '''
    Parameters
    ----------
    pg : 'string'
        A string of paragraph with more than 200 words.

    Raises
    ------
    ValueError
        If anything other than a string or a string with lower than 200 words are given, it raises value error.

    Returns
    -------
    TYPE
        If checks if there is any presence of profanity words in the given paragraph and returns True or False accordingly.
        Source of profanity words: https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt
    '''
    profanity_list=[line.strip() for line in open('profanity.txt')]
    if type(pg) != str:
        raise ValueError("Only string is allowed")
    if len(pg.split()) < 200:
        raise ValueError("String paragraph with minimum 200 words is required")
    return False or bool([p for p in pg.split() if p in profanity_list])

def reduce_sum_even(l:'list') -> 'int':
    '''
    Parameters
    ----------
    l : 'list'
        List of integers as input.

    Raises
    ------
    ValueError
        If anything other than a list or a list other than intergers are given, it raises value error.

    Returns
    -------
    TYPE
        It adds the even numbers from the list and gives the result.
    '''
    if type(l) != list:
        raise ValueError("Only a list of numbers is allowed")
    for i in l:
        if type(i) != int:
            raise ValueError("Only integers are allowed in the input list")
    return reduce(lambda a, b: a + (b if b % 2 == 0 else 0), l, 0)

def reduce_big_str(string:'str') -> 'str':
    '''
    Parameters
    ----------
    string : 'str'
        A simple string whatever printable characters.

    Raises
    ------
    ValueError
        If the input is other than string then it raises value error.

    Returns
    -------
    TYPE
        It finds the character in the string with higest ASCII number and returns that.
    '''
    if type(string) != str:
        raise ValueError("Only string is allowed")
    return reduce(lambda a, b: max(a, b), string)

def add_third_number(l:'list') -> 'int':
    '''
    Parameters
    ----------
    l : 'list'
        A list of integers.

    Raises
    ------
    ValueError
        If anything other than list or a list of other than integers are given then it raises value error.

    Returns
    -------
    TYPE
        The function adds all the elements from every third positions from each other in the list and returns the value.
    '''
    if type(l) != list:
        raise ValueError("Only a list of numbers is allowed")
    for i in l:
        if type(i) != int:
            raise ValueError("Only integers are allowed in the input list")
    return reduce(lambda a, b: a+b, l[::3])

def random_number_plates(state_code:'str'='KA') -> 'list':
    '''
    Parameters
    ----------
    state_code : 'str', optional
        A string of two capital letters. The default is 'KA'.

    Raises
    ------
    ValueError
        If anything other than a string or a string with length not equal to 2.
        If any of the characters from the string is not within A to Z

    Returns
    -------
    list
        It generates random number between 10 and 99 and another from 1000 and 9999 and concatenates them with given state code to create number plate.
        It creates 15 such random number plates and returns them as a list.
    '''
    if (type(state_code) != str) or (len(state_code) != 2):
        raise ValueError("Only a string of length two is allowed")
    for s in state_code:
        if (ord(s) < 65) or (ord(s) > 90):
            raise ValueError("Only a string of two capital letters is allowed")
    return [state_code + str(random.randint(10, 99)) + str(random.randint(1000, 9999)) for _ in range(15)]

def number_plates(state_code:'str'='KA', nl:'int'=1000, nu:'int'=9999) -> 'list':
    '''
    Parameters
    ----------
    state_code : 'str', optional
        A string of two capital letters. The default is 'KA'.. The default is 'KA'.
    nl : 'int', optional
        Lower limit of the number plate. The default is 1000.
    nu : 'int', optional
        Upper limit of the number plate. The default is 9999.

    Raises
    ------
    ValueError
        If anything other than a string or a string with length not equal to 2.
        If any of the characters from the string is not within A to Z.
        If any of lower and upper limits is not an interger.
        If lower limit is greater than upper limit.

    Returns
    -------
    list
        It generates random number between 10 and 99 and another from 1000 and 9999 and concatenates them with given state code to create number plate.
        It creates 15 such random number plates and returns them as a list.
    '''
    if (type(state_code) != str) or (len(state_code) != 2):
        raise ValueError("Only a string of length two is allowed")
    for s in state_code:
        if (ord(s) < 65) or (ord(s) > 90):
            raise ValueError("Only a string of two capital letters is allowed")
    if (type(nl) != int) or (len(str(nl)) != 4):
        raise ValueError("Lower limit has to be a four digit number")
    if (type(nu) != int) or (len(str(nu)) != 4):
        raise ValueError("Upper limit has to be a four digit number")
    if nu <= nl:
        raise ValueError("Upper limit must be greater than lower limit")
    return [state_code + str(random.randint(10, 99)) + str(random.randint(nl, nu)) for _ in range(15)]

partial_number_plates = partial(number_plates, 'DL')