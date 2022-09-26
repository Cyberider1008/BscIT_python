#fibonacci

nterm = int(input("enter nterm : "))

n1 = 0
n2 = 1
count = 2

if nterm <= 0:
    print("plz enter positive number")
elif nterm == 1:
    print(f"plz enter number above {nterm}")
    print(n1)
else:
    print(n1, n2, end=', ')
    while count < nterm:
        nth = n1 + n2
        print(nth, end=", ")
        n1 = n2
        n2 = nth 
        count += 1


