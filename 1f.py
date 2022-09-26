#Write a recursive function to print the factorial for a given number.

from tkinter import N


def recursive_func(num):
    if num == 1:
        return num
    else:
        return num * recursive_func(num -1)

num = int(input("enter a number: "))

if num < 0:
    print(f"{num} can't negative")
elif num == 0:
    print(f"{num} can't zero")
else:
    print(f"factorial of {num} is ", recursive_func(num))
