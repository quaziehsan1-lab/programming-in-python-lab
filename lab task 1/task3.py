#1111111111
a = input("Enter first value: ")
b = input("Enter second value: ")

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

#22222222
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("Distance =", distance)

#33333333333333
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#4444444444444
character = input("Enter a character: ")

if character.lower() in "aeiou":
    print("Vowel")
else:
    print("Not a vowel")

#5555555555555555555
marks = float(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 80:
    print("Grade: A+")
elif marks >= 70:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")