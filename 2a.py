'''Write a function that takes a character (i.e. a string of length 1) and
returns True if it is a vowel, False otherwise.'''

def isvowel(s):
    l = ['a', 'e', 'i', 'o', 'u']
    for i in s:
        if i in l:
            print(f'{i} is True')
        else:    
            print(f'{i} is false')

string1 = input("enter the string: ")

isvowel(string1)