'''Create a Python function named add_numbers that accepts an array of numeric types
and returns the sum of them as a float value. The function must use a for loop and must cast the numbers to floats.

Usage:

array = [1.0, 1.1, "1"]
result = add_numbers(array)
print(result)
Output:

3.1'''
def add_numbers (array): # defind the function named add_numbers that accepts a single parameter named array
    total = 0 # initializes a variable named total to 0 so it can store the sum of the numbers in the array

    for num in array:# for loop that iterates over each element num in the input array.
                    # On each iteration, the loop variable num takes the value of the current element.
        total += float(num) # This line adds the float representation of the current element num to the total
        #The float() function is used to cast num to a float before adding it to total
        #This ensures that even if the element is a string representation of a number,
                    #it will be converted to a float and added correctly.
    return total
#This line returns the final value of total as the output of the function.
# The value represents the sum of all the numbers in the input array.

#Initialize a variable total with a value of 0 to keep track of the running sum.

array = [1.0, 1.1, "1"]
result = add_numbers(array)
print(result)

# Iterate over each element num in the input array.
#
# Convert the current element num to a float using the float() function.
#
# Add the float value of num to the total using the += operator.
#
# Once all elements in the array have been processed, return the final value of total as the result of the function.