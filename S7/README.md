# EPAI Session 7

## check_fabinocci
This function takes a number and checks if that number is a fabinocci number or not. It returns True or False

## add_odd_even
The function adds corrsponding elements from the lists if element from first list is even and element from second list if odd

## strip_vowel
A string after removal of vowel characters. A simple string of characters is allowed. If anything other than a string is provided, the function raises value error.
## relu
List of intergers or floats after converting -ve number to zero. List of intergers or floats. The function raises value error if anything other than list as provided as argument.
Raises value error if any of the elements in the list is not an integer or float.

## sigmoid
List of intergers or floats after converting each number to its sigmoid value. List of intergers or floats. The function raises value error if anything other than list as provided as argument.
Raises value error if any of the elements in the list is not an integer or float.

## shift_string
The function shifts each letter in the string to its next 5th position and then concatenates them to return the updated string.
Takes a string of characters. Capital letters are allowed however the function converts them to lower characters.
Only a to z characters are considered from the given string programatically.
If anything other than a string is given then the functions raises value error.

## find_profanity
If checks if there is any presence of profanity words in the given paragraph and returns True or False accordingly.
Source of profanity words: https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt
A string of paragraph with more than 200 words.
If anything other than a string or a string with lower than 200 words are given, it raises value error.

## reduce_sum_even
It adds the even numbers from the list and gives the result.
List of integers as input.
If anything other than a list or a list other than intergers are given, it raises value error.


## reduce_big_str
It finds the character in the string with higest ASCII number and returns that.
A simple string whatever printable characters.
If the input is other than string then it raises value error.

## add_third_number
The function adds all the elements from every third positions from each other in the list and returns the value.
A list of integers.
If anything other than list or a list of other than integers are given then it raises value error.

## random_number_plates
It generates random number between 10 and 99 and another from 1000 and 9999 and concatenates them with given state code to create number plate.
It creates 15 such random number plates and returns them as a list.
A string of two capital letters. The default is 'KA'.
If anything other than a string or a string with length not equal to 2.
If any of the characters from the string is not within A to Z

## number_plates
It generates random number between 10 and 99 and another from 1000 and 9999 and concatenates them with given state code to create number plate.
It creates 15 such random number plates and returns them as a list.
Parameters:
state_code : 'str', optional
A string of two capital letters. The default is 'KA'.. The default is 'KA'.
nl : 'int', optional
Lower limit of the number plate. The default is 1000.
nu : 'int', optional
Upper limit of the number plate. The default is 9999.

Raises

ValueError
If anything other than a string or a string with length not equal to 2.
If any of the characters from the string is not within A to Z.
If any of lower and upper limits is not an interger.
If lower limit is greater than upper limit.
## partial_number_plates
calls number_plates with hard coded values for nl and nu. This accepts input only for the state code.


## test_check_fabinocci_ve
This function takes an input and checks if that is an integer or not and raises value error if not.

## test_add_odd_even_ve
This function takes two arguments. it checkes if both of them are list or not. If not then it raises value error.

## test_strip_vowel_ve
This test function checks if the input is a string or not. If not raises value error.

## test_relu_ve_list
This test function checks if the input is a list or not. If not raises value error.


## test_relu_ve_str
This test function checks if all the elements in a list are numbers or not. Raises value error if not.

## test_sigmoid_ve_list
This test function checks if the input is a list or not. If not raises value error.
## test_sigmoid_ve_str
This test function checks if all the elements in a list are numbers or not. Raises value error if not.

## test_shift_string_ve_str
This test function checks if the input is a string or not. If not raises value error.

## test_find_profanity_ve_str
This test function checks if the input is a string or not. If not raises value error.

## test_find_profanity_ve_length
This test function checks if the input is a string and length greater than or equal to 200. If not raises value error.

## test_reduce_sum_even_ve_list
This test function checks if the input is a list or not. If not raises value error.

## test_reduce_sum_even_ve_str
This test function checks if all the elements in a list are numbers or not. Raises value error if not.

## test_reduce_big_str_ve_str
This test function checks if the input is a string or not. If not raises value error.

## test_add_third_number_ve_list
This test function checks if the input is a list or not. If not raises value error.

## test_add_third_number_ve_str
This test function checks if all the elements in a list are numbers or not. Raises value error if not.

## test_random_number_plates_ve_str
This test function checks if the input is a string and of length 2. If not raises value error.

## test_number_plates_ve_str
This test function checks if the input is a string and of length 2. If not raises value error.

## test_number_plates_ve_nbr
This test function checks if the input is a number and of length 4. If not raises value error.

## test_check_fabinocci_arg
This function takes an approprioate input values and validates the output result. If that result does not match, it throws error.
## test_add_odd_even_arg
This function takes an approprioate input values and validates the output result. If that result does not match, it throws error.

## test_strip_vowel_arg
This function takes an approprioate input values and validates the output result. If that result does not match, it throws error.

## test_relu_arg
This function takes an approprioate input values and validates the output result. If that result does not match, it throws error.

## test_sigmoid_arg
This function takes an approprioate input values and validates the output result. If that result does not match, it throws error.

## test_shift_string_arg
This function takes an approprioate input values and validates the output result. If that result does not match, it throws error.

## test_find_profanity_arg
This function takes an approprioate input values and validates the output result. If that result does not match, it throws error.

## test_reduce_sum_even_arg
This function takes an approprioate input values and validates the output result. If that result does not match, it throws error.

## test_reduce_big_str_arg
This function takes an approprioate input values and validates the output result. If that result does not match, it throws error.

## test_add_third_number_arg
This function takes an approprioate input values and validates the output result. If that result does not match, it throws error.

## test_random_number_plates_arg
This function takes an approprioate input values and validates the output result. If that result does not match, it throws error.

## test_number_plates_arg
This function takes an approprioate input values and validates the output result. If that result does not match, it throws error.

## test_partial_number_plates_arg
This function takes an approprioate input values and validates the output result. If that result does not match, it throws error.
