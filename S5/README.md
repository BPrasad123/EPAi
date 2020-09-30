# EPAI Session 3

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

## test_squared_power_list_more_values
It checks if more than one numbers are given for which powers are to be raised

## test_squared_power_list_no_value
It checks if no argument is passed for which powers are to be raised

## test_squared_power_list_str_value
It checks if the argument passed is of type string for which powers are to be raised

## test_squared_power_list_extra_range
It checks if there is any additional named argument given other than start and end

## test_squared_power_list_less_range
It validates the value against start named argument is less than that of start argument

## test_squared_power_list_other_range
It checks if any other named argument is passed in stead of any of the named arguments start and end

## test_squared_power_list_str_range
It checks if values against named arguments are string or number and raise value error.

## test_squared_power_list_ls_check
It validates the value against start named argument is less than that of start argument

## test_polygon_area_nbr_exists
It checks if the input number exists as the size of the edge of the polygon

## test_polygon_area_more_nbr
It checks if more than one input numbers given as size of the edge of the polygon

## test_polygon_area_nbr_str
It checks if input value given as size of the edge of the polygon is a string

## test_polygon_area_negative_nbr
It checks if the input value for the size of the edge of the polygon is negative or not

## test_polygon_area_no_sides
It checks if any number of sides given or not for a polygon and raise value error

## test_polygon_area_more_sides
It checks if multiple inputs given for the size of the polygon and raises value error.

## test_polygon_area_negative_shape
It checks if any negative number is given for the size of the polygon.

## test_polygon_area_shape_less2
It validates the input for the polygon to ensure no number less than three is given as that is not geomatrically possible.

## test_polygon_area_shape_more6
It checks to ensure that only up to hexagon it is supported. Otherwise raises error.
## test_temp_converter_degree_exist
It checks if at all any input degree is given for the conversion to celsius.

## test_temp_converter_more_degree
It checks if more than one value is given for the conversion to celsius.

## test_temp_converter_degree_str
It checks if by any chance a string is given in place of valid degree value for conversion.

## test_temp_converter_no_temp_unit
It checks if the unit value of the temperature value is present or not.

## test_temp_converter_more_temp_unit
It checks if there are more than one units mentioned for the given degree value.

## test_temp_converter_other_arg
It checks instead of F and K if there is any other unit of temperature given.

## test_temp_converter_nbr_temp_unit
It checks a number is given against the unit of the temperature already given.

## test_temp_converter_inv_temp_unit
It checks instead of F and K if there is any other unit of temperature given.

## test_speed_converter_nbr_exist
It checks there is any value given for the distance for speed calculation.

## test_speed_converter_more_nbr
It checks if there are more than one values given as distance for speed calculation.

## test_speed_converter_str_nbr
It checks if instead of a number, a string is given as distance.

## test_speed_converter_more_arg
It checks if more than two named arguments given for the speed calculation.

## test_speed_converter_less_arg
It checks if less then two named arguments are given for the speed calculation.

## test_speed_converter_nbr_arg
If checks instead of a string, a number has been given for the unit of time or distance.

## test_speed_converter_inv_dist
It checks if valid entry is given against the time named argument when the function is called.

## test_speed_converter_inv_time
It checks if valid entry is given against the dist named argument when the function is called.

## test_squared_power_list
It gives all the valid inputs the function squared_power_list and validates is the result is accurate

## test_polygon_area
It gives all the valid inputs the function polygon_area and validates is the result is accurate

## test_temp_converter
It gives all the valid inputs the function temp_converter and validates is the result is accurate

## test_speed_converter
It gives all the valid inputs the function speed_converter and validates is the result is accurate

## test_print
It calls time_it function with print function and checks if the time taken is more than zero.