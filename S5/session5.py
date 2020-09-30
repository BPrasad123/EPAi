import time
from math import tan, pi

def squared_power_list(*args, **kwargs):
    if len(args) > 1:
        raise ValueError("Received more than 1 numbers of which powers need to be calculated. Provide only one value")
    if not len(args):
        raise ValueError("Argument missing for the number of which powers needs to be calculated.")
    nbr = args[0]
    if type(nbr) not in [int, float]:
        raise ValueError("Given number must be numeric of which powers need to be calculated")

    if len(kwargs) > 2:
        raise ValueError("Got more than two named arguments values. Only start and end positions expected.")
    if len(kwargs) < 2:
        raise ValueError("Expected start and end positions of the power range but got less number of arguments")
    a, b = kwargs
    if {a, b} != {'start', 'end'}:
        raise ValueError("Expected both start and end arguments. Either one or both of them are missing.")
    if (type(kwargs['start']) not in [int, float]) or (type(kwargs['end']) not in [int, float]):
        raise ValueError("Values for both start and end of power range must be numeric")
    if kwargs['end'] < kwargs['start']:
        raise ValueError("Ending power number cannot be smaller than the starting power number")

    result = []
    for i in range(kwargs['start'], kwargs['end']+1):
        result.append(nbr**i)

    return result

def polygon_area(*args, **kwargs):
    if not args:
        raise ValueError("Argument missing for side length of polygon.")
    if len(args) > 1:
        raise ValueError("Received more than 1 numbers for side length of polygon. Provide only one value")
    s_length = args[0]
    if type(s_length) not in [int, float]:
        raise ValueError("Side length must be numeric")
    if s_length < 0:
        raise ValueError("Side length cannot be negative")

    if not kwargs:
        raise ValueError("Argument for number of sides of polygon is missing")
    if len(kwargs) > 1:
        raise ValueError("Expected only one named argument for number of sides and its length but got more than one.")
    a, = kwargs
    if a != 'sides':
        raise ValueError(f"Expected value for named arugument 'sides' but got for unknown '{a}'")
    if type(kwargs[a]) not in [int, float]:
        raise ValueError("Polygon segments must be numeric")
    if kwargs[a] < 3:
        raise ValueError("Polygon cannot have less than three sides")
    if kwargs[a] > 6:
        raise ValueError("This function can only support up to a hexagon. You may want to reduce number of sides now.")

    p_area = kwargs[a] * (s_length ** 2) / (4 * tan(pi / kwargs[a]))

    return p_area

def temp_converter(*args, **kwargs):
    if not args:
        raise ValueError("Argument missing for base temperature degree.")
    if len(args) > 1:
        raise ValueError("Received more than 1 numbers for base temperature.")
    degree = args[0]
    if type(degree) not in [int, float]:
        raise ValueError("Temperature degree must be numeric")

    if not kwargs:
        raise ValueError("Argument missing for unit of base temperature: temp_given_in")
    if len(kwargs) > 1:
        raise ValueError("Expected only one named argument in total but got more than one.")
    a, = kwargs
    if a != 'temp_given_in':
        raise ValueError(f"Expected value for named arugument 'temp_given_in' but got for unknown '{a}'")
    if type(kwargs['temp_given_in']) not in [str]:
        raise ValueError("Unit of temperature must be a string")
    if kwargs['temp_given_in'].lower() not in ['f', 'k']:
        raise ValueError("Unit of base temperature must be 'f' for Fahrenheit or 'k' for Kelvin")

    c_temp = round((degree - 32) * 5 / 9)

    return c_temp

def speed_converter(*args, **kwargs):
    if not args:
        raise ValueError("Argument missing for distance.")
    if len(args) > 1:
        raise ValueError("Received more than 1 numbers for distance")
    nbr = args[0]
    if type(nbr) not in [int, float]:
        raise ValueError("Distance must be numeric")

    if len(kwargs) > 2:
        raise ValueError("Got more than two named arguments. Only 'dist' and 'time' are allowed.")
    if len(kwargs) < 2:
        raise ValueError("Expected two named arguments but got less.")
    a, b = kwargs
    if {a, b} != {'dist', 'time'}:
        raise ValueError("Expected both 'dist' and 'time' arguments. Either one or both of them are missing.")
    if (type(kwargs['dist']) not in [str]) or (type(kwargs['time']) not in [str]):
        raise ValueError("Units for both dist and time must be string")
    if kwargs['dist'] not in ['km', 'm', 'ft', 'yrd']:
        raise ValueError("Unit of distance must be one of km/m/ft/yrd")
    if kwargs['time'] not in ['ms', 's', 'min','hr', 'day']:
        raise ValueError("Unit of time must be one of ms/s/m/hr/day")

    if kwargs['dist'] == 'm':
        nbr = nbr * 0.001
    elif kwargs['dist'] == 'ft':
        nbr = nbr * 0.0003048
    elif kwargs['dist'] == 'yrd':
        nbr = nbr * 0.0009144

    if kwargs['time'] == 'day':
        speed = nbr / 24.0
    elif kwargs['time'] == 'min':
        speed = nbr * 60.0
    elif kwargs['time'] == 's':
        speed = nbr * 60.0 * 60.0
    elif kwargs['time'] == 'ms':
        speed = nbr * 60.0 * 60.0 * 1000.0

    return speed

def time_it(fn, *args, repetitions= 1, **kwargs):
    start_time = time.time()
    for r in range(repetitions):
        _ = fn(*args, **kwargs)
    end_time = time.time()
    r = format(((end_time - start_time) / repetitions), '.25f')
    print(r)
    return r
