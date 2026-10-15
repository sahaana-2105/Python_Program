#strings-collection of characters and immutable
name="naveen"
dept="python"
print(name)
print(dept)
print(dept[0])
print(dept[1])
print(dept[-1])
print(dept[:3])
print(dept[2:6])
print(dept[0:4])
print(dept[::-1])

a="python"
a="j"+a[1:]
print(a)
print(len(a))
for ch in a:
    print(ch,end=" ")
print()
text="java programming"
print(text.upper())
print(text.lower())
print(text.replace("java","python"))
print(text.count('a'))
print(text.find("programming"))
print(text.find("c"))
print(text.startswith("java"))
print(text.endswith("programming"))

text1="                 java programming               "
print(text1.strip())
text2="java python nodejs"
courses=text2.split()
print(courses)

text3=["python","java","c++"]
text4=",".join(text3)
print(text4)