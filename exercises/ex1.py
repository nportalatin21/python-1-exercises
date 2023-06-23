'''
# Ex. 1 Hello World
Create a Python function named `hello_world` that accepts a string
that represents the number of times the following message is
printed on the console: `Hello World from Python!`.  This function
must convert the string to an integer and must use a for loop to
    print the message to the console.

Usage:
```python
hello_world("3")
```

Output:

Hello World from Python!
Hello World from Python!
Hello World from Python!

def ex1():
    print("who's there")
'''

def hello_world(num):  # Defines a function named hello_world that accepts a single parameter named num
    num = int(num) # converts the num parameter from a string to int, the converstion is needed because range() requires a int as input
    for _ in range(num): #starts a for loop that will iterate num a number of times. The _ is a placeholder for the loop since the
                        # value is not needed within the loop
        print("Hello World!") # prints the string three times to the console

hello_world("3") # calls the hello_world function and passes the argument "3". The message will be printed three times

"""Overall the function takes a string representing the number of times to print the message, 
converts it to an integer, and then uses a for loop to print the message that many times. 
 The functgion call at the end executes the function with the desired argument and produces the expected output"""
