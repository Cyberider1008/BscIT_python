#Implement the concept of inheritance using python

class A:
    def __init__(self):
       print("Class of A")

class B(A):
    def child(self):
        print("class of B")

b = B()
b.child()

