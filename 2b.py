#Define a function that computes the length of a given list or string.

def total_str(str):
    count = 0 
    
    for i in str:
        if i != ' ':
            count += 1
    print(f"total number of string is {count}")

str1 = "god is the great"
total_str(str1)