# for loop

for i in range(10):
    print("Hello Keerthana")

for i in range(1,11):
    print(i)

for i in range(1,101,3):
    print(i,end=" ")
print()
for i in range(5,0,-1):
    print(i)

# print by adding the gn nos
num=int(input("Enter number: "))
total=0
for i in range(1,num+1):
    total+=i
print(total)

print 
num1=int(input("Enter F Num"))
num2=int(input("Enter S Num"))
totals=0
for i in range(num1,num2):
    totals=0
    for i in range(num1,num2+1):
        if i%2==0:
            totals+=i
print(totals)

# multiplication table
num=int(input("Enter the no "))
for i in range(1,11):
    mul=i*num
    print(i,"*",num,"=",mul)
    # or
num=int(input("Enter the no "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)

num=int(input())
fact=1
for i in range(1,num+1):
    fact=fact*i
    print(i,end=" ")
    if i<num:

        print("*",end=" ")
print("=",fact)

n=int(input())
digits=0
total=0
while n!=0:
    rem=n%10
    digits+=1
    total=total+rem
    n=n//10
print("No.of digits: ",digits)
print("Sum of digits: ",total)