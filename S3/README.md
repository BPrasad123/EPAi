# EPAI Session 3

## int
int is a class in Python that takes string or number of any base and converts that to integer of base 10. The default base argument is 10.

## encoded_from_base10
This function basically takes a number of base 10 and converts that to a number of any base between 2 and 36 inclusive. The encoded values for the converted number can be mapped as per the third argument passed to the function. 
The function returns the encoded value in string format.

## digit_map
digit_map is the third parameter in the function encoded_from_base10. This gives the flexibity to encode values of any number of any base to any set of unique characters. The number of items in the digit_map must match with the base number passed to the function.

## ValueError
If has been put in the functions to raise execption messages during edit checks. It helps the programmer or user to put in the right argument value.

## math
It is a python package that comes with a collection predefined mathemetical functions for ease of usage. However, in the assignment to practise the use cases, we created equivalant functions corresponding to that of math packages wherever needed.

## isclose
It is a function of math package that helps in comparing two numbers considering the tolerance limits as specificed by both absolute and relative limits. It actually combines both of these limits by taking their maximum and comparing against the actual different between original two numbers.

## absolute
If is a hard coded very small value set by the programmer as a threshold for the difference between two numbers to be considered as equal. Although it works for certain numbers however, for very numbers it fails to do the job.

## relative
Well, instead of just considering only the hard coded limit as in absolute limit, here that number is a percentage of the maximum between two original numbers. This way, the limit wil vary based on the magnitude of the numbers being compared. However, when the number is very close to zero, it fails to do the job.

## tolerance
tolerance is more generic that denots the threshold of delta between two numbers to be considered as equal.

## bin()
It is a class that converts a string, integer or float to binary format that is a number of base 2. 

## hex()
It is a class that converts a string, integer or float to hexadecimal format that is a number of base 14.

## round
It is python function that approximates a float number to its most close integer value. 

## truncation
Truncation is basically removing a logical part of a string or number. math.trunc is a function that only returns the number prior to the decimal point without any approximation.

## error
If any syntactic issue is there in the code the system invokes predefined corresponding error message. Moreover, we can put in edit checks in the code to raise an error if certain conditions are not met.

## equality
It is basically a comparison of two values (may be of two variables but not variables themselves). Since the numbers are stored in the binary format in python, the actually value might very slightly vary from the original value. Considering this delta we can specify a threshold limit while comparing to numbers.

## zero
It is a number that carries different values depending upon its positino in a number.

## away
It basically quantifies the difference between two numbers.



