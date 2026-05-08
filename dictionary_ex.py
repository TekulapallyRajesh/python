students={ 1 : {"name": "rajesh", "age":21,"department":"csm"},
           2 : {"name": "vishal", "age":23,"department":"cse" }
}
students["city"]="Hyderabad"
students["age"]=25

students.pop("city")
print(students)
print("_______________________________________________________________----")
print(students.keys())

print("_______________________________________________________________----")
print(students.items())
print("_______________________________________________________________----")
print(students.values())
print("_______________________________________________________________----")
for key,values in students.items():
    print(key,values)

print("_______________________________________________________________----")

print(students[2]["name"])

