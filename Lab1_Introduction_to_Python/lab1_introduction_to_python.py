# Lab 1 - Introduction to Python
# 1. Variables and Data Types
name = "Alice"
age = 21
gpa = 3.85
is_student = True
print(f"Name: {name}, Age: {age}, GPA: {gpa}, Student: {is_student}")
# 2. Arithmetic Operations
x, y = 10, 3
print(f"Add: {x+y}, Sub: {x-y}, Mul: {x*y}, Div: {x/y:.2f}")
print(f"Modulus: {x%y}, Power: {x**y}")
# 3. String Operations
sentence = "Python is amazing"
print(sentence.upper())
print(len(sentence))
print(sentence.replace("amazing", "powerful"))
print(sentence.split())
# 4. Lists
fruits = ["apple", "banana", "cherry", "date"]
fruits.append("elderberry")
print(fruits)
print(fruits[1:3]) # Slicing
# 5. Dictionary
student = {"name": "Bob", "age": 20, "marks": 85}
for key, value in student.items():
    print(f"{key}: {value}")
# 6. Simple Calculator
a, b = 15, 4
print(f"{a}+{b}={a+b}, {a}-{b}={a-b}, {a}*{b}={a*b}, {a}/{b}={a/b:.2f}")
