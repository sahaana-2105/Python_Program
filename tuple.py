# #tuple ordered immutable allow duplicate
tuple_1=(34,67,89,23)
print(tuple_1)
print(type(tuple_1))

tuple_2=(5,)
print(type(tuple_2))

tuple_3=(12,45,67,89,23)
for data in tuple_3:
    print(data,end=" ")
print()
i=0
while i<len(tuple_3):
    print(tuple_3[i],end=" ")
    i+=1
print()
tuple_4=(1,2,3,2,3,1)
print(tuple_4.count(3))
print(tuple_4.index(3))

print(len(tuple_4))
print(sum(tuple_4))
print(min(tuple_4))

tuple=(10,20,10,30,20,40)
for i in set(tuple):
    if tuple.count(i)>1:
        print(i)
