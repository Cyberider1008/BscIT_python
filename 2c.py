'''Define a procedure histogram() that takes a list of integers and prints a
histogram to the screen. For example, histogram([4, 9, 7]) should print the
following:'''


def histogram(l1):
    for i in l1:
        print('*' * i)

l1 = [4 ,9, 7]
histogram(l1)