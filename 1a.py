'''Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will
turn 100 years old.'''

import datetime as d

name = input("plz enter ur name: ")
print("hello "+name)
age = int(input("plz enter your age: "))
current_year = d.datetime.now().year
print("current year is ", current_year)
print("u will turn 100 in ",str(int(100-age)+int(current_year)))
