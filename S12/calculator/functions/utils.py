# utils.py

def print_f(func):
    def inner(*args,**kwargs):
        result=func(*args,**kwargs)
        print(f"Result of {func.__name__}: {result}")
        return result
    return inner
