'''Create a Python function named array_to_string that accepts an array of ints and returns a string. The function must use a for loop and must cast the ints to strings.

Usage:

array = [1, 2, 3]
result = array_to_string(array)
print(result)
Output:

1 2 3
'''

def array_to_string(array):# Defines a function named array_to_string that accepts a single parameter named array
                            # the array parameter represents the input array of integers
    string_list = [] # initializes an empty list called string_list. This will be used to store the string
                      # representations of the integers in the input array
    for num in array: # starts a for loop that iterates over each element num in the input array.
                    # on each iteration, the loop variable num takes the value of the current element
        string_list.append(str(num)) # converts the current int num to a string using the str() function.
                                # The resulting string is appended to the string_list using the append() method
                                # This ensures that the string representation of each integer is added to the list
    return' '.join(string_list)
#the join() method is ued to link together all the strings in the string_list, separating them with a space ' '
# The join() method takes the string_list and links its elements using the specified separator. The resulting string is
#then returned as the output of the function.


array = [1, 2, 3]
result = array_to_string(array)
print(result)