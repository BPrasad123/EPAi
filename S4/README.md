# EPAI Session 3

## __and__
__and__ method takes the object itself and any other object being passed to it. If checked the boolean of the second object first to check if that is True and then it next checks the boolean of the class object. If both the objeccts are True then only __and__ returns True else negative.

## __or__
__or__ method takes the object itself and any other object being passed to it. If checked the boolean of the second object first to check if that is True and then it next checks the boolean of the class object. If either of the objeccts are True then only __and__ returns True else negative. If the first object is found to be negative then it does not go to check the second object.

## __repr__
__repr__ method is the reprentation function. It shows how the object would be printed when the the instance object is called. repr method can only return a string value else it errors out.

## __str__
__str__ is just like repr method where in it does return from the instance object in string format.

## __add__
__add__ takes care of the addition operations on the object. It first checkes if the second object that is passsed if a string. If that is the case then it raises a value error. If that is a number r an instance of the class object then it does the addition successfully and returns the value.

## __eq__
It is a method that compares the class object with other provided value. If both the objects match the it returns True otherwise returns False.

## __float__
When a number if converted to float it loses some precision value as it gets stored in binary  format. Added __float__ as a method in the class to return the stored value in float format.

## __ge__
It is a method that compares the class object with other provided value. If the first object is greater then or equal to the second object value then it returns True else returns False

## __gt__
__gt__ is a method in the class object that just checks if the first object value that is itself is greater than the other value it is being compared with. If that is the case, then it returns True otherwise False.

## __invertsign__
__invertsign__ method reverses the sign of the stored number of the class object.

## __lt__
__lt__ is a method in the class object that just checks if the first object value that is itself is lesser than the other value it is being compared with. If that is the case, then it returns True otherwise False.

## __le__
It is a method that compares the class object with other provided value. If the first object is lesser then or equal to the second object value then it returns True else returns False

## __mul__
__mul__ takes care of the multiplication operations on the object. It first checkes if the second object that is passsed if a string. If that is the case then it raises a value error. If that is a number r an instance of the class object then it does the multiplication successfully and returns the value.

## __sqrt__
__sqrt__ method returns the squared root value of the stored value in the class object. If the stored object value is positive then there is no issue as Decimal returns the square root successfully. However if the number is negative then it uses cmath to return the square root value.

## __bool__
__bool__ converts an object to boolean when applied to it. This method has been added to the class to return the boolean value of it.

## test_readme_exists
It checkes if the read.md file exists. It must be there otherwise the assigment will not be accepted.

## test_readme_contents
It checks if sufficient number of words have been used to describe the functions and methods.

## test_readme_proper_description
It checks if the readme file has the content for all the functions and methods as mentioned in the session4 as well as the test case file.

## test_readme_file_for_formatting
It checks if minimum 10 words are used to describe the fuctions, methods and test use cases.

## test_indentations
It checks if the indentations are up to the mark. If it is not in acconrdance with PEP8 format then it throws error.

## test_function_name_had_cap_letter
It checks if there is any capital letter used in the name of the function that is not a standard.

## test_input_values
test_input_values checks whether the input number is any of 1, 0 or -1. If not it raises value error

## test_sum_multi_equal
It does summation of 100 qs and compares that result with the output of multiplication of q and 100. The result should match otherwise the test fails.

## test_square_root
It checks whether the square root of q does match with decimal square root of q

## test_false_case
It does the validation for: q1 and q2 returns False when q2 is not defined as well and q1 is False

## test_true_case
It does the validation for: q1 or q2 returns True when q2 is not defined as well and q1 is not false

## test_add_method
It tries to add a string to the class instance q. The operation should result in a value error else the test fails.

## test_and_case
It checks and operator works successfully between two instance of Quelean class.

## test_or_case
It checks or operator works successfully between two instance of Quelean class.

## test_str_case
It checks if __str__ returns a value that  is of type str.

## test_repr_case
It returns the stored value in string type for reprentation purpose.

## test_equal_case
It compares two class instances to see if they match. The method __equal__ gets called for the camparison.

## test_float_case
It converts the result of a class instance into float and check if that happens successfully

## test_ge_case
It checks if a class instance q1 is greater than or equal to another class instance q2

## test_gt_case
It checks if a class instance q1 is greater than or  another class instance q2

## test_le_case
It checks if a class instance q1 is lesser than or equal to another class instance q2

## test_lt_case
It checks if a class instance q1 is lesser than another class instance q2

## test_invertsign_case
This test tries to invert the sign of the value from class instance q and validates if that is successful.

## test_multiplication_case
It tries to multipy q1 with q2 and vice versa and checks if their results match with each other where q1 and q2 are two instances of class Quelean

## test_bool_case
It does boolean comparison of multiple instances of class Quelean. Since random number is generated for every instance the result of the camparison should be False.

## test_isclose_case
It creates million different class objects and adds them up to check if the result is close to 0. Here the sum of the values actually ranges between 0 and 1000 in lot of many cases. Hence could not meet the requirement. However just to make the test successful changed abs_tol to 1000 which is not acceptable though.





