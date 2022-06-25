def fib(n):
    if(n<=1):
        return 0
    elif(n==3 or n==2):
        return 1
    else:
        return fib(n-1)+ fib(n-2)

n=int(input("Digite um valor: "))
fib(n)
print("O número é {}".format(fib(n)))

