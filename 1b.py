# Python program to check if the input number is odd or even.
# A number is even if division by 2 give a remainder of 0.
# If remainder is 1, it is odd number.

num = int(input("enter the number: "))

if num%2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
