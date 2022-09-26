'''Write a Python program to print a specified list after removing the 0th,
2nd, 4th and 5th elements.'''


l1=[1,2,3,4,5,6,7,8,9,0]
print("Original List is",l1)
l1.remove(l1[0])
l1.remove(l1[1])
l1.remove(l1[2])
l1.remove(l1[2])