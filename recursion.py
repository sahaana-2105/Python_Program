
#recursion-function calling itself
def greet(n):
    if n==0:
        return
    print("Hello")
    greet(n-1)
greet(5)
def counts(num):
    if num==11:
        return
    print(num)
    counts(num+1)
counts(1)
#recursion_factorial
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
n=int(input())
result=factorial(n)
print(result)