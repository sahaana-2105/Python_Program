num1=int(input("Enter a no:"))
if num1>0:
    print("POSITIVE")
elif num1<0:
    print("NEGATIVE")
else:
    print("ZERO")

a=int(input("Enter a first no:"))
b=int(input("Enter a second no:"))
c=int(input("Enter a third no:"))
if a>=b and a>=c:
    print("Greatest",a)
elif b>=a and b>=c:
    print("Greatest,b")
else:
    print("Greatest",c)


amount=float(input("Enter purchase amount:"))
if amount < 0:
    print("Invalid amount")
else:
    discount=0.0
    if amount>=5000:
        discount=amount*20/100
    elif amount>=2000 and amount <5000:
        discount=amount*10/100
    print("Discount amount:",discount)
    print("Final payable amount:",amount-discount)
