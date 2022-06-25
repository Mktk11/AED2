'''Questão 1: Implemente o algoritmo para calcular o n-ésimo elemento da sequência de Fibonacci visto em aula na linguagem de sua preferência (Python, C ou C++). 
Execute o programa para n = 10, 20, 30, …, 100, 200, 300, ..., 1000. Apresente a implementação proposta e um relatório detalhando se os cálculos foram 
corretamente realizados para todos os valores de n testados e quais dificuldades foram encontradas.'''

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

