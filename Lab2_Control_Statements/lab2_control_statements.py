# Lab 2 - Control Statements
# 1. If-Elif-Else: Grade Calculator
marks = 78
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"
print(f"Marks: {marks} -> Grade: {grade}")
# 2. For Loop: Multiplication Table
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")
# 3. While Loop: Factorial
n, factorial, i = 5, 1, 1
while i <= n:
    factorial *= i
    i += 1
print(f"Factorial of {n} = {factorial}")
# 4. Nested Loop: Star Pattern
for i in range(1, 6):
    print("* " * i)
# 5. Break and Continue
for num in range(1, 21):
    if num % 6 == 0:
        continue # skip multiples of 6
    if num > 16:
        break # stop at 16
    if num % 2 == 0:
        print(num, end=" ")
print()
# 6. List Comprehension
squares = [x**2 for x in range(1, 11)]
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Squares:", squares)
print("Evens:", evens)
# 7. FizzBuzz
for n in range(1, 21):
    if n % 15 == 0: print("FizzBuzz", end=" ")
    elif n % 3 == 0: print("Fizz", end=" ")
    elif n % 5 == 0: print("Buzz", end=" ")
    else: print(n, end=" ")
print()
