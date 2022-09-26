# reverse number


import mailbox


def reverse_num(num):
    sum = 0 
    while(num>0):
        new_num = num % 10
        sum = (sum * 10) + new_num
        num = num // 10
    
    print(sum)

num = int(input("enter the number: "))
reverse_num(num)
