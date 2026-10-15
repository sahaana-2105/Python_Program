
#Exception Handling
try:
    a=int(input())
    b=int(input())
    c=a//b
    print(c)
except ZeroDivisionError:
    print("Please enter positive number")
except ValueError:
    print("Enter positive integer")
finally:
    print("Java Programming")