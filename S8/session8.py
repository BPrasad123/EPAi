'''
Assignment 8:

Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable - 200
Write a closure that gives you the next Fibonacci number - 100
We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts - 250
Modify above such that now we can pass in different dictionary variables to update different dictionaries - 250

'''

def docstring_check_closure(n:'int') -> 'function':
    '''
    Parameters
    ----------
    n : 'int'
        Takes a number as input. This number is used to check if enough number of characters are there in the docstring.

    Returns
    -------
    Returns a function
    '''
    def count_docstring(fn: 'function'):
        '''
        Parameters
        ----------
        fn : 'function'
            It takes a function and checks if it has a docstring. If then checks if number of characters in the docstring
            is more then the number obtained as free variable from the closure.

        Returns
        -------
        bool
            True or False depending upon the number of characters in the docstring.
        '''
        if fn.__doc__:
            if len(fn.__doc__) > n:
                return True
            else:
                return False
        else:
            return False
    return count_docstring


docstring_check = docstring_check_closure(50)

def func_with_docstring(param: 'str') -> 'None':
    '''
    Parameters
    ----------
    param : TYPE
        DESCRIPTION. This is just a dummy function to be checked if it has docstring or not.

    Returns
    -------
    None.
    '''
    return None

def func_without_docstring(param: 'str') -> 'None':
    return None

def func_with_less_docstring(param: 'str') -> 'None':
    '''
    dummy doctstring
    '''
    return None

# docstring_check_closure(func_with_docstring)
# docstring_check_closure(func_without_docstring)


def next_fibonacci() -> 'function':
    '''
    Returns
    -------
    TYPE
        Closure function that returns fabinocci function with next fibonacci number.
    '''
    fib_nbrs = [0, 1]
    counter = 0
    def fabinocci() -> 'int':
        '''
        Returns
        -------
        nbr : TYPE
            Function to uses free variable from the closure function and generates next fibonacci number.
        '''
        nonlocal fib_nbrs
        nonlocal counter
        if counter == 0:
            nbr = fib_nbrs[0]
            counter += 1
        elif counter == 1:
            nbr = fib_nbrs[1]
            counter += 1
        else:
            nbr = fib_nbrs[-1] + fib_nbrs[-2]
            fib_nbrs.append(nbr)
        return nbr
    return fabinocci

next_fibonacci_closure = next_fibonacci()


func_count_dict = {'add': 0, 'mul': 0, 'div':0}


def func_counter() -> 'functions':
    '''
    Closure function that returns add, mul and div functions.
    '''
    def add(a:'int', b:'int') -> 'int':
        '''
        Parameters
        ----------
        a : 'int'
            First number to be used in addition.
        b : 'int'
            Second number to be used in addition.

        Returns
        -------
        TYPE
            Sum of first and second numbers.
        '''
        global func_count_dict
        func_count_dict[add.__name__] += 1
        return a+b

    def mul(a:'int', b:'int') -> 'int':
        '''
        Parameters
        ----------
        a : 'int'
            First number to be used in multiplication.
        b : 'int'
            Second number to be used in multiplication.

        Returns
        -------
        TYPE
            Multiplication result of first and second numbers.
        '''
        global func_count_dict
        func_count_dict[mul.__name__] += 1
        return a*b

    def div(a:'int', b:'int') -> 'int':
        '''
        Parameters
        ----------
        a : 'int'
            First number to be used in Division.
        b : 'int'
            Second number to be used in division.

        Returns
        -------
        TYPE
            Division result of first by second numbers.
        '''
        global func_count_dict
        func_count_dict[div.__name__] += 1
        return a/b

    return add, mul, div


add, mul, div = func_counter()



def update_dict_closure(d: 'dict') -> 'functions':
    '''
    Parameters
    ----------
    d : 'dict'
        A dictionary that needs to be updated with counter for the called function.

    Returns
    -------
    It is a closure function that returns three functions 
    '''
    d = {'add2': 0, 'mul2': 0, 'div2':0}
    def add2(a:'int', b:'int') -> 'int':
        '''
        Parameters
        ----------
        a : 'int'
            First number to be used in addition.
        b : 'int'
            Second number to be used in addition.

        Returns
        -------
        TYPE
            Sum of first and second numbers.
        '''
        nonlocal d
        d[add2.__name__] += 1
        print(f"Function 'add2' has been called {d[add2.__name__]} times")
        return a+b, add2.__name__, d[add2.__name__]

    def mul2(a:'int', b:'int') -> 'int':
        '''
        Parameters
        ----------
        a : 'int'
            First number to be used in multiplication.
        b : 'int'
            Second number to be used in multiplication.

        Returns
        -------
        TYPE
            Multiplication result of first and second numbers.
        '''
        nonlocal d
        d[mul2.__name__] += 1
        print(f"Function 'mul2' has been called {d[mul2.__name__]} times")
        return a*b, mul2.__name__, d[mul2.__name__]

    def div2(a:'int', b:'int') -> 'int':
        '''
        Parameters
        ----------
        a : 'int'
            First number to be used in Division.
        b : 'int'
            Second number to be used in division.

        Returns
        -------
        TYPE
            Division result of first by second numbers.
        '''
        nonlocal d
        d[div2.__name__] += 1
        print(f"Function 'div2' has been called {d[div2.__name__]} times")
        return a/b, div2.__name__, d[div2.__name__]

    return add2, mul2, div2


dict1 = {'add2': 0, 'mul2': 0, 'div2':0}
dict2 = {'add2': 0, 'mul2': 0, 'div2':0}

add2, mul2, div2 = update_dict_closure(dict1)

add3, mul3, div3 = update_dict_closure(dict2)












