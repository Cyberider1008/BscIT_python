'''Write a function to check the input value is Armstrong and also write the
function for Palindrome.'''


def armstrong(num):
    sum = 0
    temp = num
    while temp >0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        print(f"{num} is armstrong")
    else:
        print(f"{num} is not armstrong")


def palindrome(num):
    n =num
    rev = 0
    while num != 0:
        rev = rev * 10
        rev =rev + int(num % 10)
        num //= 10
    if rev == n:
        print(f"{n} is palindrome ")
    else:
        print(f"{n} is not palindrome ")
        


num = int(input("Enter a number to chk it is armstrong or not: "))
armstrong(num)

num = int(input("Enter a number to chk it is palindrome or not: "))
palindrome(num)
