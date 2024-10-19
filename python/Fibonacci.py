def fib(num):
    a1 = 0
    a2 = 1
    print(a1,a2,end = " ")
    for i in range(2,num):
        a1,a2 = a2,a1+a2
        print(a2, end=" ")
n = int(input("Enter how many members of fibonacci series you want displayed: "))
fib(n)