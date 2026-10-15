a=0
b=1
print(a,"",b,end=" ")
for i in range(3,11):
    c=a+b
    print(c,end="")
    a=b
    b=c
print()
def fib(num):
    if num==0 or num==1:
        return num
    return fib(num-1)+fib(num-2)
num=int(input())
print(fib(num))