'''A pangram is a sentence that contains all the letters of the English alphabet
at least once, for example: The quick brown fox jumps over the lazy dog.
Your task here is to write a function to check a sentence to see if it is a
pangram or not.'''

import string

def ispangram(str1):
    alphabets = string.ascii_lowercase
    for char in alphabets:
        if char not in str1:
            return False
    return True

string1 = 'the quick brown fox jumps over the lazy dog'

if(ispangram(string1) == True):
    print("Yes")
else:
    print("No")
