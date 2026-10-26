#11111111111
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#222222222222
number = int(input("Enter a number: "))

while number >= 0:
    print(number)
    number = number - 1

#333333333333
number = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

answer = number ** exponent

print("Answer:", answer)

#44444444444
total = 0

for number in range(2, 1000):
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        total = total + number

print("Sum:", total)

#5555555555
n = int(input("Enter N: "))

first = 0
second = 1

while first < n:
    print(first)
    next_number = first + second
    first = second
    second = next_number