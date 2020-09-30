# EPAI Session 9

# test_check_with_docstring
This function checks if all the functions in the script have docstring or not.

# test_oadd_oddrun
This test function calls oadd function that is a decorated function that runs only on the odd second. The test function validates the number of run times in a loop to confirm.

# test_mul
This test function checks if the output value from the function is correct. The decorated function returns the timestamp of the execution time.

# test_authenticate
This test function checks if the authentication function raises value error when incorrect password is given. If incorrect, the function should not execute.

# test_fib_reduce
This test function validates the output from fabinocci reduce function. The decorated function is designed to give average execution time based on number of runs.

# test_get_access
This test function validates output for given privilage profile. It checks 'high' as a privilage value to confirm.

# test_htmlize_complex_numbers
This test function checks the html value for a given number of complex type.

# oddrun
This is decoration function that allows a function to execute only if the current second time value is odd.

# oadd
This is a decorated function that returns sum value of given numbers. Due to the decoration, the function executes only if the cuurent time is odd in second.

# logged
This is decoration function that decorates an inner function with timestamp value and returns the inner function.

# mul
It is a simple function to return multiplied value of given input numbers. It is decorated with logged function to give the timestamp as well as of execution time.

# set_password
It is a function that takes password as input as stores as a free variable. the function ideally should have taken the input from interaction, however for the submission purpose it has been hard coded. The function returns the password when called.

# authenticate
It is a decoration function that validates input password with already stored value (in free variable from set_password) and based on validation executes the given function.

# timed
It is decoration function that runs an inner function for given number of times and then takes their run times to generate average execution time.

# fib_reduce
It is a function that generates fibonacci number. It leverages reduce function with lambda to do so.

# set_profiles
This function uses decoration and closure similar to set_password function. It creates privilage corresponding access profile in a dictionary as a free variable.

# grant_access
It is a decoration function that uses the privilage dictionary as a free variable and passes that to inner function and returns it.

# get_access
This function is assigned to inner closure function from grant_access. It is decorated with access profile diction returned from grant_access. It returns access profile for a given privilage level.

# htmlize
This function returns the html representation of a value of certain data type. It is decorated with singledispatch.

# htmlize_complex_numbers
This function is regiseted with htmlize by calling htmlize.regiseter(). This can generate html representation for a given number of type complex.