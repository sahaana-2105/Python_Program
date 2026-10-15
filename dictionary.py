
#Dictionary mutable,collection of key value pairs key unique values repeat

student1={
    "name":"naveen",
    "age":20,
    "mark":459,
    "dept":"ece"
}

print(student1)
print(student1["name"])
print(student1["age"])
print(student1.get("mark"))
print(student1.get("city","not applicable"))
student1["mark"]=499
print(student1)
student1["city"]="pondy"
print(student1)
student1.pop("age") 
print(student1)

for a,b in student1.items(): 
    print(a,":",b)