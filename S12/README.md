# EPAI Session 10

# test_funcs_with_docstring
This test function checks all the functions from session10 script and checks if all those have doc string defined. If any of the functions do not have doc string then it raises error. In the script all the functions does have proper doc string defined, hence the test is not failing.

# test_timed_reps_type_check
This test function calls timed_reps function with input parameter as a text. However there is an edit check in the function to raise value error if theinput is of any type other than int. Since the given input is a string, the function raises value error as expected. The test passes as the error is raised as per expectation.

# test_create_random_profiles_type_check
This test function calls create_random_profiles function with input parameter as a text. However there is an edit check in the function to raise value error if theinput is of any type other than int. Since the given input is a string, the function raises value error as expected. The test passes as the error israised as per expectation.

# test_d_create_random_profiles_type_check
This test function calls d_create_random_profiles function with input parameter as a text. However there is an edit check in the function to raise value error if theinput is of any type other than int. Since the given input is a string, the function raises value error as expected. The test passes as the error israised as per expectation.

# test_stock_exchange_type_check
This test function calls stock_exchange function with input parameter as a text. However there is an edit check in the function to raise value error if theinput is of any type other than int. Since the given input is a string, the function raises value error as expected. The test passes as the error israised as per expectation.

# test_stock_exchange
This test function calls stock_exchange function that returns a pandas dataframe. This test case validates all the high values are actually greater than open, close and low values for all the instances. If any of them fail, in that case the test fails.

# calculate_age
This is function that simply takes date of birth in datetime format and calculates the age as of running date. 

# timed_reps
This is a decorator function that taken n as input and runs the given function n number of times to find the average run time of the function. It can be applied to any function to print the average run time of the associated function.

# create_random_profiles
Creates n as input and creates n number of fake profiles. Each profile is stored as a namedtuple in a list. It calculates most frequent blood group, average location, oldest person and average age and returns them. Decorated with timed_reps to run the function 20 times to get the average run time.
# d_create_random_profiles
Creates n as input and creates n number of fake profiles. Each profile is stored as a dictionary in a list. It calculates most frequent blood group, average location, oldest person and average age and returns them. Decorated with timed_reps to run 20 times to get average run time.
# stock_exchange
Takes n as input and creates n number of random company names using Faker. Calls company_symbol function to create 5 character symbol for the company.
Creates random values to assign open, high, low and close stock values however adhering to comparison rules. Puts the company stock details in pandas dataframe to print in tabular form.
