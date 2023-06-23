

def replace_period(sentence, new): # Function named replace_period that accepts two parameters: sentence and new
    # sentence and new. The sentence parameter represents the input sentence, and the new parameter represents
    # the punctuation character that will replace the period.

    sentence2 = sentence.replace(".", new) # This line creates a new string sentence2 by using the replace() method
    # on the sentence string. The replace() method replaces all occurrences of the period (".") in the sentence string
    # with the specified new punctuation character. The resulting modified string is assigned to sentence2.


    return sentence2 # This line returns the modified string sentence2 as the output of the function.


sentence = "Test.  This is a test.  Testing."
sentence2 = replace_period(sentence, "!")
print(sentence2)






# FUNCTION replace_period(sentence, new):
#     sentence2 = REPLACE all occurrences of "." in sentence WITH new
#     RETURN sentence2


# Replace all occurrences of the period (".") in the input sentence with the specified new punctuation character.
# This operation can be performed using the REPLACE operation.
#
# Store the modified sentence in a variable named sentence2.
#
# Return the value of sentence2 as the output of the function, representing the sentence with the replaced period.