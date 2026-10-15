# set  - unique unordered mutable
numbers={1,2,3,6,4,3,2}
print(numbers)
names={"Abilash","Basha","David","Elango"}
print(names)
empty_set=set()#create empty set
empty_set={45,67,89}
print(empty_set)

nums1={10,20,30,40}
print(nums1)
nums1.add(50)
print(nums1)
nums1.update([60,70,80])
print(nums1)

nums2=[1,2,3,1,2,3,3,2,4,67,567]
unique_set=set(nums2)
print(unique_set)

nums3={56,78,90,34,12}
nums3.remove(56)
print(nums3)
nums3.discard(12)
print(nums3)
#nums3.remove(100)
#print(nums3)
nums3.discard(100)
print(nums3)
nums3.clear()
print(nums3)

nums4={1,2,3,4,5,6,7,8,9}
for value in nums4:
    print(value,end=" ")
print()
a={1,2,3,3}
b={3,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))