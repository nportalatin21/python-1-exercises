

def count_words(sentence): #This line defines a function named count_words that accepts a single parameter sentence.
    # The parameter represents the input sentence provided by the user

    words = sentence.split() #split() method on the sentence string to split it into a list of words.
    #The split() method splits the string at whitespace characters (including multiple consecutive spaces)
    # and returns a list of words. By not passing any argument to split(), it defaults to splitting at whitespace.

    return len(words) # len() function to calculate the length of the words list. The len() function
    # returns the number of elements (in this case, words) in the list.
    # This represents the number of words in the sentence.


sentence = input("Enter sentence: ")
num_words = count_words(sentence)
print(num_words)

# puedo code:
# Split the input sentence sentence into a list of words by using the SPLIT operation,
# specifying whitespace as the separator. This operation splits the sentence at each whitespace character,
# including multiple consecutive spaces, and returns a list of words.
#
# Calculate the number of words in the list by using the LENGTH OF operation,
# which returns the count of elements in the list. Store this count in a variable named num_words.
#
# Return the value of num_words as the output of the function,
# representing the number of words in the sentence.


#FUNCTION count_words(sentence):
# words = SPLIT sentence BY whitespace
# num_words = LENGTH OF words
# RETURN num_words
